from .models import (
    DiagnosticIssue
)


from .rules import (
    KSAMPLER_RULES
)



class ParameterChecker:


    # KSampler widgets 顺序:
    # [seed, control, steps, cfg, sampler_name, scheduler, denoise]
    KSAMPLER_KEYS = [
        "seed",
        "control",
        "steps",
        "cfg",
        "sampler_name",
        "scheduler",
        "denoise"
    ]



    def extract_params(
        self,
        node
    ):


        # 参数值存放在 widgets（parser 已捕获），
        # inputs 里只有输入定义（name/type/link）
        if node.widgets:

            return {
                k: v
                for k, v in zip(
                    self.KSAMPLER_KEYS,
                    node.widgets
                )
            }


        return (
            node.inputs
            if isinstance(
                node.inputs,
                dict
            )
            else {}
        )



    def check_node(
        self,
        node
    ):


        issues=[]



        if node.node_type=="KSampler":


            params=self.extract_params(
                node
            )



            cfg=params.get(
                "cfg"
            )


            if cfg:


                if cfg > KSAMPLER_RULES["cfg"]["high"]:


                    issues.append(

                    DiagnosticIssue(

                    issue_type=
                    "parameter_warning",

                    severity=
                    "medium",

                    node=
                    "KSampler",

                    parameter=
                    "cfg",

                    value=
                    str(cfg),


                    message=
                    "CFG值较高，可能导致Prompt约束过强",


                    suggestion=
                    "建议尝试CFG 7-10"

                    )

                    )



            steps=params.get(
                "steps"
            )


            if steps:


                if steps < KSAMPLER_RULES["steps"]["low"]:


                    issues.append(

                    DiagnosticIssue(

                    issue_type=
                    "parameter_warning",

                    severity=
                    "medium",

                    node=
                    "KSampler",

                    parameter=
                    "steps",

                    value=
                    str(steps),


                    message=
                    "Steps较低，可能导致细节不足",


                    suggestion=
                    "建议增加到20-30"

                    )

                    )



        return issues
