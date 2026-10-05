"""
知识蒸馏器

把知识卡全文压成几行「与本问题相关」的内容。

为什么需要：
    检索召回的知识条目 content 是知识卡**全文**（ksampler.md 有 241 行，
    包含输入引脚图、初学者比喻、学习任务等），直接塞进回答没人看得下去。
    这里按问题关键词与节点名定位到相关小节，只保留参数说明、常见错误、
    注意事项这类真正回答「为什么 / 怎么办」的部分。

不调 LLM，纯规则：按 Markdown 标题切段，再按相关度排序取前 N 段。
"""

import re
from typing import List, Dict, Any, Tuple


# 段落相关度权重：标题命中这些词时，该段对「为什么/怎么办」类问题最有价值
HIGH_VALUE_HEADINGS = (
    "常见错误", "注意", "风险", "常见问题", "问题",
    "参数", "影响", "过高", "过低", "调整", "优化", "建议",
    "作用", "位置", "输出", "说明", "限制", "解决",
)

# 这些段落对回答问题基本没用，直接丢弃
LOW_VALUE_HEADINGS = (
    "学习任务", "练习", "实验", "任务", "延伸", "参考", "资源",
    "流程图", "位置",
)

# 段落里的行内标记，转纯文本时去掉
_INLINE_NOISE = re.compile(r"[`*>#\[\]()]")


class KnowledgeDistiller:
    """
    知识卡全文 → 精简相关片段
    """

    def __init__(self, max_sections: int = 3, max_chars: int = 600) -> None:
        """
        初始化蒸馏器

        Args:
            max_sections: 最多保留几个小节
            max_chars: 单个回答的总字符上限，防止把整张卡塞进来
        """
        self.max_sections = max_sections
        self.max_chars = max_chars

    # ---------- 切段 ----------

    @staticmethod
    def split_sections(content: str) -> List[Tuple[str, str]]:
        """
        按 Markdown 标题切段

        Args:
            content: Markdown 全文

        Returns:
            [(标题, 正文)]

        实现说明：
            知识卡结构是「# 节点名 / ## 参数组 / ## 具体参数名」，
            具体参数名往往是 H2 而非 H3（如 `## cfg`），若只记当前标题，
            分组信息（`## 核心参数`）会丢失。所以额外记录 H1 作为根标题，
            给每个小节标题加上根前缀，蒸馏结果才看得懂「cfg 属于哪个节点」。

            只有标题没有正文的小节（纯分组标题）会被丢弃 ——
            它们产出不了任何内容，留着只会稀释相关性评分。
        """
        if not content:
            return []

        sections: List[Tuple[str, str]] = []
        root_title = ""
        current_title = ""
        current_body: List[str] = []

        def flush():
            body = "\n".join(current_body).strip()
            if not body:
                return
            title = current_title
            if root_title and title and root_title not in title:
                title = f"{root_title} · {title}"
            elif not title:
                title = root_title
            sections.append((title, body))

        for line in content.splitlines():
            heading = KnowledgeDistiller._heading_of(line)

            if heading is not None:
                level, title = heading

                if level == 1:
                    # H1 是节点名，重新开始
                    flush()
                    root_title = title
                    current_title = title
                    current_body = []
                else:
                    flush()
                    current_title = title
                    current_body = []
            else:
                current_body.append(line)

        flush()

        return sections

    @staticmethod
    def _heading_of(line: str):
        """
        判断是否为 Markdown 标题

        Returns:
            (层级, 标题文字)；不是标题则返回 None
        """
        stripped = line.strip()
        if not stripped.startswith("#"):
            return None

        level = len(stripped) - len(stripped.lstrip("#"))
        title = stripped[level:].strip()
        if not title:
            return None

        return level, title

    # ---------- 评分 ----------

    def score_section(
        self,
        title: str,
        body: str,
        keywords: List[str]
    ) -> float:
        """
        给小节打相关度

        Args:
            title: 小节标题
            body: 小节正文
            keywords: 问题关键词（小写）

        Returns:
            分数，越高越相关
        """
        lowered_title = title.lower()
        lowered_body = body.lower()
        score = 0.0

        # 标题命中高价值词
        for hint in HIGH_VALUE_HEADINGS:
            if hint in lowered_title:
                score += 3.0
                break

        # 标题命中低价值词：重罚
        for hint in LOW_VALUE_HEADINGS:
            if hint in lowered_title:
                score -= 8.0
                break

        # 标题直接命中关键词，权重最高
        for keyword in keywords:
            if keyword and keyword in lowered_title:
                score += 10.0

        # 正文提及关键词
        body_hits = sum(
            1 for keyword in keywords
            if keyword and keyword in lowered_body
        )
        score += body_hits * 1.5

        # 过短的段落信息量不足
        if len(body) < 40:
            score -= 2.0

        return score

    def distill(
        self,
        content: str,
        question: str = "",
        extra_keywords: List[str] = None
    ) -> str:
        """
        蒸馏知识卡

        Args:
            content: 知识卡 Markdown 全文
            question: 用户问题
            extra_keywords: 额外关键词（节点类型、参数名等）

        Returns:
            精简后的纯文本片段
        """
        if not content:
            return ""

        keywords = self._keywords_of(question, extra_keywords)
        sections = self.split_sections(content)

        if not sections:
            return self._plain(content)

        scored = [
            (self.score_section(title, body, keywords), title, body)
            for title, body in sections
        ]
        # 分数为负的段落（学习任务等）直接丢
        relevant = [s for s in scored if s[0] > 0]
        relevant.sort(key=lambda x: -x[0])

        if not relevant:
            # 全都不相关就取最长的一段，至少给点内容
            relevant = sorted(scored, key=lambda x: -len(x[2]))[:1]

        lines: List[str] = []
        total = 0

        for score, title, body in relevant[:self.max_sections]:
            snippet = self._condense(title, body)

            if not snippet:
                continue

            block = f"{title}：{snippet}" if title else snippet

            if total + len(block) > self.max_chars:
                remaining = self.max_chars - total
                if remaining > 60:
                    lines.append(block[:remaining] + "…")
                break

            lines.append(block)
            total += len(block)

        if not lines:
            return self._plain(content, limit=200)

        return "\n".join(lines)

    # ---------- 文本处理 ----------

    def _condense(self, title: str, body: str) -> str:
        """
        把小节正文压成单行要点
        """
        points = self.extract_points(body)
        if not points:
            return ""
        return "；".join(points)

    def extract_points(self, body: str) -> List[str]:
        """
        从正文里抽出要点

        识别三种常见写法：
            * 列表项   * xxx / - xxx
            裸行        采样次数。
            代码值      单独一行的短值（20、KSampler 等），跳过

        另外过滤两类噪声：
            - 纯序号式短片段（「step 1」「更多」单独成行），拼成句子没有意义
            - 以冒号结尾的引导语（「它负责：」后面紧跟内容），单独出现是断句

        Args:
            body: 小节正文

        Returns:
            要点列表
        """
        points: List[str] = []

        for raw in body.splitlines():
            line = raw.strip()
            if not line:
                continue

            # 分隔线
            if set(line) <= {"-", "*", "=", "—"} and len(line) >= 3:
                continue

            # 代码块内容一律跳过（是值不是解释）
            if line.startswith("`") and line.endswith("`"):
                continue

            # 标题行
            if line.startswith("#"):
                continue

            if line.startswith(("-", "*", "+")):
                text = self._clean(line.lstrip("-*+ ").strip())
            elif line.startswith(">"):
                text = self._clean(line.lstrip("> ").strip())
            else:
                text = self._clean(line)

            if not self._is_meaningful(text):
                continue

            points.append(text)

        return points[:6]

    @staticmethod
    def _is_meaningful(text: str) -> bool:
        """
        判断一条要点是否值得保留
        """
        if len(text) < 2:
            return False

        # 纯数值 / 纯符号
        if re.fullmatch(r"[\d.\-+%]+", text):
            return False

        # 「step 1」「euler」这类序号或单个术语，拼进句子读不通
        if re.fullmatch(r"[A-Za-z]+ ?\d*", text) and len(text) <= 8:
            return False

        # 以冒号结尾的引导语，单独出现是断句（「它负责：」）
        if text.endswith(("：", ":")):
            return False

        # 太短的中文片段，信息量不足
        if len(text) <= 3 and not re.search(r"[\u4e00-\u9fff]{2,}", text):
            return False

        return True

    def _keywords_of(
        self,
        question: str,
        extra_keywords: List[str] = None
    ) -> List[str]:
        """
        组装关键词表
        """
        keywords = []

        if question:
            # 按非中文字符切词，英文节点名才能命中标题
            tokens = re.findall(r"[A-Za-z][A-Za-z0-9_+\-]{1,}", question)
            keywords.extend(t.lower() for t in tokens)

            # 中文按 2-gram 粗切，够用且无需分词器
            chinese = re.findall(r"[\u4e00-\u9fff]{2,}", question)
            for run in chinese:
                for i in range(len(run) - 1):
                    keywords.append(run[i:i + 2])

        if extra_keywords:
            keywords.extend(str(k).lower() for k in extra_keywords if k)

        return [k for k in keywords if len(k) >= 2]

    @staticmethod
    def _clean(text: str) -> str:
        """
        去掉行内 Markdown 标记
        """
        return _INLINE_NOISE.sub("", text).strip()

    def _plain(self, content: str, limit: int = 200) -> str:
        """
        兜底：无法切段时返回截断的纯文本
        """
        text = self._plain_text(content)
        return text[:limit] + ("…" if len(text) > limit else "")

    @staticmethod
    def _plain_text(content: str) -> str:
        """
        全文转纯文本
        """
        out = []
        in_code = False

        for line in content.splitlines():
            stripped = line.strip()

            if stripped.startswith("```"):
                in_code = not in_code
                continue

            if in_code:
                continue

            if not stripped or set(stripped) <= {"-", "*", "="} and len(stripped) >= 3:
                continue

            out.append(KnowledgeDistiller._clean(stripped))

        return " ".join(out)
