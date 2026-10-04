from .models import (
    DiagnosticIssue
)



class GraphChecker:



    def check(
        self,
        graph
    ):


        issues=[]



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
