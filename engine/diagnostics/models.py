from dataclasses import dataclass, field

from typing import List



@dataclass
class DiagnosticIssue:


    issue_type:str


    severity:str


    node:str=""


    parameter:str=""


    value:str=""


    message:str=""


    suggestion:str=""




@dataclass
class DiagnosticReport:


    workflow_type:str=""


    issues:List[DiagnosticIssue]=field(
        default_factory=list
    )


    suggestions:List[str]=field(
        default_factory=list
    )



    def add_issue(
        self,
        issue
    ):

        self.issues.append(
            issue
        )
