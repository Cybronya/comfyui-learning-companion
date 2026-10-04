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
        workflow_json
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


        return {


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
