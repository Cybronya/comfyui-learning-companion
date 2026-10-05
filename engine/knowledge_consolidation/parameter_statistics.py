"""
参数统计

按模式分组统计参数，而不是全局混算。

设计稿的做法是把所有 workflow 的参数收进一个 defaultdict 求平均，
再把**同一份**结果贴给每个模式。这有两个问题：

    1. 数值没有意义。SD1.5 的 steps 集中在 20-30，
       若样本里混进一个 Wan 视频 workflow（steps=50），均值就失去代表性。
    2. 所有模式的参数完全一样，等于没做分组统计 ——
       「ControlNet 流程 CFG 偏高、img2img 流程 denoise 偏低」
       这种真正的规律反而看不出来。

所以统计的输入是**单个模式的成员**，由 ConsolidationEngine 逐模式调用。

另外补了中位数与集中度：
    - 均值会被单个异常值拉偏，中位数更能代表「典型取值」
    - 集中度低说明这组 workflow 参数五花八门，
      此时给出的「典型区间」不可信，recommendations 里会相应降级
"""

from collections import Counter, defaultdict
from typing import List, Dict, Any

from .models import ParameterStat
from .experience_loader import ExperienceRow


# 只统计这些参数：其余（如 checkpoint 路径）没有归纳价值
# 扩展性考虑：这里是白名单而非黑名单，避免把 seed 这类纯随机值算进知识
INTERESTING_PARAMS = (
    "cfg",
    "steps",
    "denoise",
    "sampler_name",
    "scheduler",
    "width",
    "height",
    "controlnet_strength",
    "strength_model",
    "strength_clip",
)

# 随机参数：值本身无规律，统计了反而误导
NOISE_PARAMS = {"seed", "batch_size"}


class ParameterStatistics:
    """
    参数统计器
    """

    def __init__(
        self,
        interesting_params: List[str] = None
    ) -> None:
        """
        初始化统计器

        Args:
            interesting_params: 需要统计的参数名；None 时用默认白名单
        """
        self.interesting_params = (
            list(interesting_params)
            if interesting_params is not None
            else list(INTERESTING_PARAMS)
        )

    def analyze(
        self,
        experiences: List[ExperienceRow]
    ) -> Dict[str, ParameterStat]:
        """
        统计一组 workflow 的参数

        Args:
            experiences: 同一模式内的成员记录

        Returns:
            {参数名: ParameterStat}
        """
        buckets: Dict[str, List[Any]] = defaultdict(list)

        for row in experiences:
            for name, value in (row.parameters or {}).items():
                if name not in self.interesting_params:
                    continue
                if name in NOISE_PARAMS:
                    continue
                if value is None:
                    continue
                buckets[name].append(value)

        stats: Dict[str, ParameterStat] = {}

        for name, values in buckets.items():
            stats[name] = self._build_stat(name, values)

        return stats

    def _build_stat(
        self,
        name: str,
        values: List[Any]
    ) -> ParameterStat:
        """
        单个参数的统计

        数值与字符串分开处理：
            数值 → min/max/mean/median + 集中度
            字符串（sampler_name 等）→ 最常用值
        """
        if not values:
            return ParameterStat()

        numeric = [
            v for v in values
            if isinstance(v, (int, float)) and not isinstance(v, bool)
        ]
        textual = [str(v) for v in values if v not in numeric]

        # 全是数值（或数值占绝大多数）才算数值统计
        if numeric and len(numeric) >= len(textual):
            return self._numeric_stat(name, numeric, textual)

        counter = Counter(str(v) for v in values)
        most_common, top_count = counter.most_common(1)[0]

        return ParameterStat(
            count=len(values),
            most_common=most_common,
            values=list(values),
            # 单一取值占比即集中度
            consistency=(
                top_count / len(values) if values else 0.0
            ),
        )

    @staticmethod
    def _numeric_stat(
        name: str,
        numeric: List[float],
        textual: List[str] = None
    ) -> ParameterStat:
        """
        数值参数统计
        """
        ordered = sorted(numeric)
        count = len(ordered)

        if count % 2 == 1:
            median = ordered[count // 2]
        else:
            median = (ordered[count // 2 - 1] + ordered[count // 2]) / 2

        mean = sum(ordered) / count

        # 集中度：1 - 变异系数，上限截到 [0,1]。
        # 均值为 0 时无法定义变异系数（如 denoise 恒为 0），此时用极差判断：
        # 全部相同则 1.0，否则 0.0。
        if mean:
            spread = (
                sum((v - mean) ** 2 for v in ordered) / count
            ) ** 0.5
            consistency = max(0.0, min(1.0, 1.0 - spread / abs(mean)))
        else:
            consistency = 1.0 if ordered[0] == ordered[-1] else 0.0

        counter = Counter(str(v) for v in (textual or []))
        most_common = (
            counter.most_common(1)[0][0] if counter else None
        )

        return ParameterStat(
            count=count,
            min=ordered[0],
            max=ordered[-1],
            mean=mean,
            median=median,
            consistency=consistency,
            most_common=most_common,
            values=list(numeric),
        )

    def compare_across(
        self,
        grouped: Dict[str, List[ExperienceRow]]
    ) -> List[str]:
        """
        跨模式对比同一参数

        找出「不同流程的参数偏好不同」这类规律 ——
        这是全局混算永远看不到、而分组统计才能得到的知识。

        Args:
            grouped: {模式名: 成员列表}

        Returns:
            对比结论列表
        """
        observations: List[str] = []

        for param in self.interesting_params:
            per_pattern = {}

            for name, members in grouped.items():
                values = []
                for row in members:
                    value = (row.parameters or {}).get(param)
                    if isinstance(value, (int, float)) \
                            and not isinstance(value, bool):
                        values.append(value)

                if len(values) >= 2:
                    ordered = sorted(values)
                    mid = len(ordered) // 2
                    median = (
                        ordered[mid] if len(ordered) % 2 == 1
                        else (ordered[mid - 1] + ordered[mid]) / 2
                    )
                    per_pattern[name] = (median, len(values))

            # 至少两个模式才有对比意义
            if len(per_pattern) < 2:
                continue

            medians = {k: v[0] for k, v in per_pattern.items()}
            highest = max(medians, key=medians.get)
            lowest = min(medians, key=medians.get)

            # 差异要有实际意义，否则只是噪声
            high_v, low_v = medians[highest], medians[lowest]
            if high_v == low_v:
                continue
            if abs(high_v) > 0 and \
                    abs(high_v - low_v) / abs(high_v) < 0.2:
                continue

            observations.append(
                f"{param} 各模式中位数："
                + "、".join(
                    f"{name} {median:g}"
                    for name, (median, _count) in sorted(
                        per_pattern.items(),
                        key=lambda kv: kv[1][0],
                        reverse=True,
                    )
                )
                + f"（{highest} 最高，{lowest} 最低，"
                  f"相差 {abs(high_v - low_v):g}）"
            )

        return observations
