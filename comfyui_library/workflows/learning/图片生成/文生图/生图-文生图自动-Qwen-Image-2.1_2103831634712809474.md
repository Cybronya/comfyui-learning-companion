---
key: 生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json
name: 生图-文生图自动-Qwen-Image-2.1_2103831634712809474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json
hash: e6e911cceff98ca9
coverage: 0.515152
learned_at: 2026-10-10 20:59:53
nodes: [EmptyImage, easy int, StringFunction|pysssss, easy showAnything, Text Multiline, easy positive, SetNode, StringFunction|pysssss, easy saveText, easy positive, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, easy seed, easy int, easy int, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, CLIPLoader, easy showAnything, GetImageSizeAndCount, SaveImage, easy showAnything, GetNode, TextGenerateLTX2Prompt, KSampler, easy anythingIndexSwitch]
patterns: []
missing: [StringFunction|pysssss, StringFunction|pysssss, Text Multiline, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy saveText, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 449590870957583, "steps": 50, "width": 1024}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/生图-文生图自动-Qwen-Image-2.1_2103831634712809474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `EmptyImage`
- `easy int`
- `StringFunction|pysssss`
- `easy showAnything`
- `Text Multiline`
- `easy positive`
- `SetNode`
- `StringFunction|pysssss`
- `easy saveText`
- `easy positive`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy seed`
- `easy int`
- `easy int`
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
- `SaveImage`
- `easy showAnything`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `easy anythingIndexSwitch`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `449590870957583`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（17/33）

**有卡**：`EmptyImage`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`GetImageSizeAndCount`、`SaveImage`、`TextGenerateLTX2Prompt`、`KSampler`

**缺卡**（11）：`StringFunction|pysssss`、`StringFunction|pysssss`、`Text Multiline`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy saveText`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、TextGenerateLTX2Prompt

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
