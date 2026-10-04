from .models import (
    DiagnosticIssue
)



class QualityChecker:



    def check(
        self,
        workflow
    ):


        issues=[]



        if workflow.task_type=="text_to_image":


            if len(
                workflow.nodes
            ) < 5:


                issues.append(

                DiagnosticIssue(

                issue_type=
                "workflow_warning",

                severity=
                "low",

                message=
                "Workflow结构较简单",

                suggestion=
                "确认是否缺少必要处理节点"

                )

                )



        return issues
