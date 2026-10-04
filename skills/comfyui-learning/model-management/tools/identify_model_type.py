import os


def identify(name):

    n = name.lower()

    if "lora" in n:
        return "lora"

    if "vae" in n:
        return "vae"

    if any(
        x in n
        for x in [
            "wan",
            "hunyuan",
            "ltx",
            "video"
        ]
    ):
        return "diffusion_model"

    return "checkpoint"
