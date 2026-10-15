---
key: 图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json
name: 生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json
hash: 2c0a3c39068caef2
coverage: 0.848485
learned_at: 2026-10-15 22:28:58
nodes: [EmptyImage, easy saveText, SetNode, easy positive, easy positive, easy showAnything, llama_cpp_parameters, llama_cpp_model_loader, StringFunction|pysssss, easy int, StringFunction|pysssss, llama_cpp_instruct_adv, easy seed, Text Multiline, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, CLIPLoader, easy showAnything, GetImageSizeAndCount, easy showAnything, GetNode, TextGenerateLTX2Prompt, KSampler, SaveImage, easy imageRemBg, DapaoImageRatioLimitNode, easy anythingIndexSwitch]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 580801359318692, "steps": 50, "width": 1024}
---

# 图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `EmptyImage`
- `easy saveText`
- `SetNode`
- `easy positive`
- `easy positive`
- `easy showAnything`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `StringFunction|pysssss`
- `easy int`
- `StringFunction|pysssss`
- `llama_cpp_instruct_adv`
- `easy seed`
- `Text Multiline`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `easy showAnything`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `SaveImage`
- `easy imageRemBg`
- `DapaoImageRatioLimitNode`
- `easy anythingIndexSwitch`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `580801359318692`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`EmptyImage`、`easy saveText`、`easy positive`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`StringFunction|pysssss`、`easy int`、`llama_cpp_instruct_adv`、`easy seed`、`Text Multiline`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`GetImageSizeAndCount`、`TextGenerateLTX2Prompt`、`KSampler`、`SaveImage`、`easy imageRemBg`、`DapaoImageRatioLimitNode`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、easy seed
