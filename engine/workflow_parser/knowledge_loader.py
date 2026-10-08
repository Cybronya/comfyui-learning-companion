import json
from pathlib import Path


class NodeKnowledgeLoader:


    def __init__(
        self,
        knowledge_path
    ):

        self.knowledge_path = Path(
            knowledge_path
        )

        self.index = {}

        # 知识卡正文缓存（node_type -> markdown）。
        # load_markdown 每次都 exists()+open()+read()，批量学习时
        # 同一节点类型会被反复加载（4000 个 workflow、每种节点
        # 平均出现几十次 → 数万次重复读盘）。卡片文件运行期不变，
        # 读一次缓存即可
        self._markdown_cache = {}

        self.load_index()



    def load_index(self):

        index_file = (
            self.knowledge_path
            /
            "node_index.json"
        )


        with open(
            index_file,
            "r",
            encoding="utf-8"
        ) as f:

            data=json.load(f)


        self.index=data.get(
            "nodes",
            {}
        )



    def get_node_info(
        self,
        node_type
    ):

        return self.index.get(
            node_type
        )



    def load_markdown(
        self,
        node_type
    ):


        if node_type in self._markdown_cache:
            return self._markdown_cache[node_type]


        node_info = (
            self.get_node_info(
                node_type
            )
        )


        if not node_info:
            self._markdown_cache[node_type] = None
            return None



        file_name = (
            node_info[
                "knowledge_file"
            ]
        )


        file_path = (
            self.knowledge_path
            /
            "nodes"
            /
            file_name
        )


        if not file_path.exists():

            self._markdown_cache[node_type] = None

            return None



        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        self._markdown_cache[node_type] = content

        return content



    def load(
        self,
        node_type
    ):


        info = self.get_node_info(
            node_type
        )


        if not info:

            return None



        knowledge = info.copy()


        knowledge[
            "node_type"
        ] = node_type


        knowledge[
            "content"
        ] = self.load_markdown(
            node_type
        )


        return knowledge
