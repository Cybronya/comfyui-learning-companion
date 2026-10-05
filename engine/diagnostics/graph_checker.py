from .models import (
    DiagnosticIssue
)



class GraphChecker:



    def check(
        self,
        graph
    ):


        issues=[]



        # graph 由 WorkflowAnalyzer.analyze(include_graph=True) 提供，
        # 但不是所有调用方都会构建它（如只关心参数体检的场景会传 None）。
        # 缺 graph 时只跳过图结构检查，不让整个体检崩掉。
        if graph is None:

            return issues



        nodes=[

            n.node_type

            for n in graph.nodes.values()

        ]



        if "KSampler" in nodes:


            if "VAEDecode" not in nodes:


                issues.append(

                DiagnosticIssue(

                issue_type=
                "missing_node",

                severity=
                "high",

                node=
                "VAEDecode",

                message=
                "发现KSampler但没有VAEDecode",

                suggestion=
                "添加VAEDecode完成latent转换"

                )

                )



        return issues
