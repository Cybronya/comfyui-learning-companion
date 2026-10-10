---
key: 生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json
name: 生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json
hash: 2c0a3c39068caef2
coverage: 0.545455
learned_at: 2026-10-10 20:59:53
nodes: [EmptyImage, easy saveText, SetNode, easy positive, easy positive, easy showAnything, llama_cpp_parameters, llama_cpp_model_loader, StringFunction|pysssss, easy int, StringFunction|pysssss, llama_cpp_instruct_adv, easy seed, Text Multiline, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, CLIPLoader, easy showAnything, GetImageSizeAndCount, easy showAnything, GetNode, TextGenerateLTX2Prompt, KSampler, SaveImage, easy imageRemBg, DapaoImageRatioLimitNode, easy anythingIndexSwitch]
patterns: []
missing: [StringFunction|pysssss, StringFunction|pysssss, Text Multiline, easy anythingIndexSwitch, easy imageRemBg, easy int, easy positive, easy positive, easy saveText, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 580801359318692, "steps": 50, "width": 1024}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 生图-文生图(角色白底图四视图)-Qwen-Image-2.1_2103831644149997569.json

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

覆盖率 **55%**（18/33）

**有卡**：`EmptyImage`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`GetImageSizeAndCount`、`TextGenerateLTX2Prompt`、`KSampler`、`SaveImage`、`DapaoImageRatioLimitNode`

**缺卡**（10）：`StringFunction|pysssss`、`StringFunction|pysssss`、`Text Multiline`、`easy anythingIndexSwitch`、`easy imageRemBg`、`easy int`、`easy positive`、`easy positive`、`easy saveText`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、TextGenerateLTX2Prompt

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
