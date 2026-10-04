from .models import (
    DiagnosticReport
)


from .parameter_checker import (
    ParameterChecker
)


from .graph_checker import (
    GraphChecker
)


from .quality_checker import (
    QualityChecker
)




class DiagnosticEngine:



    def __init__(self):

        self.parameter_checker=(
            ParameterChecker()
        )

        self.graph_checker=(
            GraphChecker()
        )

        self.quality_checker=(
            QualityChecker()
        )



    def analyze(
        self,
        workflow,
        graph
    ):


        report=DiagnosticReport(

            workflow_type=
            workflow.task_type

        )



        # 参数检查

        for node in workflow.nodes:


            issues=self.parameter_checker.check_node(
                node
            )


            for issue in issues:

                report.add_issue(
                    issue
                )



        # 图结构检查

        for issue in self.graph_checker.check(
            graph
        ):

            report.add_issue(
                issue
            )



        # 工作流检查

        for issue in self.quality_checker.check(
            workflow
        ):

            report.add_issue(
                issue
            )



        # 汇总建议（去重保序）
        report.suggestions = list(
            dict.fromkeys(
                issue.suggestion
                for issue in report.issues
                if issue.suggestion
            )
        )


        return report
