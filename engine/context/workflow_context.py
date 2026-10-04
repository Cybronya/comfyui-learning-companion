from pathlib import Path



class WorkflowContext:


    def set_workflow(
        self,
        store,
        workflow_knowledge
    ):


        store["current_workflow"] = (
            Path(
                workflow_knowledge.workflow_id
            ).stem
        )


        store["workflow_nodes"] = list(
            dict.fromkeys(
                n.node_type
                for n in workflow_knowledge.nodes
            )
        )


        # 从 KSampler 提取核心生成参数
        store["workflow_parameters"] = (
            self.extract_parameters(
                workflow_knowledge
            )
        )



    def extract_parameters(
        self,
        workflow_knowledge
    ):


        # KSampler widgets 顺序:
        # [seed, control, steps, cfg, sampler_name, scheduler, denoise]
        keys = [
            "seed",
            "control",
            "steps",
            "cfg",
            "sampler_name",
            "scheduler",
            "denoise"
        ]


        for node in workflow_knowledge.nodes:

            if (
                node.node_type == "KSampler"
                and
                node.widgets
            ):

                return {
                    k: v
                    for k, v in zip(
                        keys,
                        node.widgets
                    )
                    if k in ("steps", "cfg", "sampler_name", "scheduler", "denoise")
                }


        return {}
