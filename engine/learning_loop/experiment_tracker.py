"""
实验跟踪器

负责保存实验过程和学习经验
"""

import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime
from .models import LearningExperience


class ExperimentTracker:
    """
    实验跟踪器
    """

    def __init__(self, store_path: str = "engine/learning_loop/experience_store.json"):
        """
        初始化实验跟踪器

        Args:
            store_path: 经验存储路径
        """
        self.path = Path(store_path)
        self.data: List[LearningExperience] = []
        self.load()

    def load(self) -> None:
        """
        从文件加载经验数据
        """
        if self.path.exists():
            try:
                with open(
                    self.path,
                    "r",
                    encoding="utf-8"
                ) as f:
                    data = json.load(f)

                # 转换为 LearningExperience 对象
                self.data = [
                    LearningExperience.from_dict(item)
                    for item in data
                ]
            except Exception as e:
                print(f"加载经验数据失败: {e}")
                self.data = []
        else:
            self.data = []

    def save(self) -> None:
        """
        保存经验数据到文件
        """
        try:
            # 转换为字典
            data_dict = [
                exp.to_dict()
                for exp in self.data
            ]

            # 确保目录存在
            self.path.parent.mkdir(parents=True, exist_ok=True)

            with open(
                self.path,
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    data_dict,
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except Exception as e:
            print(f"保存经验数据失败: {e}")

    def add_experience(
        self,
        experience: LearningExperience
    ) -> None:
        """
        添加学习经验

        Args:
            experience: 学习经验对象
        """
        # 如果没有时间戳，使用当前时间
        if not experience.timestamp:
            experience.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.data.append(experience)
        self.save()

    def get_all_experiences(
        self,
        workflow_type: str = None
    ) -> List[LearningExperience]:
        """
        获取所有经验（可选过滤）

        Args:
            workflow_type: 工作流类型过滤

        Returns:
            经验列表
        """
        if workflow_type:
            return [
                exp for exp in self.data
                if exp.workflow_type == workflow_type
            ]
        return self.data.copy()

    def get_recent_experiences(
        self,
        count: int = 10
    ) -> List[LearningExperience]:
        """
        获取最近的经验

        Args:
            count: 数量

        Returns:
            经验列表
        """
        return self.data[-count:] if count > 0 else []

    def clear(self) -> None:
        """清空所有经验"""
        self.data = []
        self.save()

    def get_statistics(self) -> Dict:
        """
        获取统计信息

        Returns:
            统计数据
        """
        total = len(self.data)

        # 按工作流类型统计
        type_counts = {}
        for exp in self.data:
            type_counts[exp.workflow_type] = type_counts.get(exp.workflow_type, 0) + 1

        # 按标签统计
        tag_counts = {}
        for exp in self.data:
            for tag in exp.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        return {
            "total_experiences": total,
            "by_workflow_type": type_counts,
            "by_tag": tag_counts,
        }
