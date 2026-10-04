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


        node_info = (
            self.get_node_info(
                node_type
            )
        )


        if not node_info:
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

            return None



        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()



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
