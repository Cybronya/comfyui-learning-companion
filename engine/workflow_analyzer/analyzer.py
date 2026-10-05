from .graph_builder import (
    GraphBuilder
)


from .connection_analyzer import (
    ConnectionAnalyzer
)


from .pattern_detector import (
    PatternDetector
)


from .workflow_classifier import (
    WorkflowClassifier
)




class WorkflowAnalyzer:



    def __init__(self):

        self.builder=GraphBuilder()

        self.connection=ConnectionAnalyzer()

        self.pattern=PatternDetector()

        self.classifier=WorkflowClassifier()



    def analyze(
        self,
        workflow_json,
        include_graph=False
    ):


        graph=self.builder.build(
            workflow_json
        )


        connections=self.connection.analyze(
            graph
        )


        node_types=[

            n.node_type

            for n in graph.nodes.values()

        ]


        patterns=self.pattern.detect(
            node_types
        )


        result={


        "nodes":

        node_types,


        "connections":

        connections,


        "patterns":

        patterns,


        "workflow_type":

        self.classifier.classify(
            patterns
        )


        }

        # agent_core 的诊断环节需要 graph 本身（DiagnosticEngine.analyze
        # 第二个参数），但 graph 不便序列化，所以只在显式要求时附带。
        if include_graph:
            result["graph"]=graph

        return result
