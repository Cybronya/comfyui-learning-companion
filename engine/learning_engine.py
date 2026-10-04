from .workflow_loader import WorkflowLoader


class LearningEngine:

    def __init__(self):
        self.loader = WorkflowLoader()

    def learn_workflow(
        self,
        workflow_path: str
    ):

        workflow = self.loader.load(
            workflow_path
        )

        return {
            "status": "success",
            "workflow": workflow.id,
            "nodes": len(workflow.nodes),
            "message": "Workflow loaded successfully"
        }
