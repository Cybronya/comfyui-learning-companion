---
key: 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json
name: 生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json
hash: 1b3684f1214f6ad3
coverage: 0.409938
learned_at: 2026-10-21 00:55:06
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, easy saveText, SetNode, SetNode, GetNode, Reroute, SetNode, easy positive, ImageLoader, easy int, SetNode, GetNode, MemoryCleaner, GetNode, EmptyImage, easy seed, easy int, easy int, llama_cpp_parameters, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, EmptyLatentImage, ImpactInt, ImpactInt, CLIPLoader, SetNode, VAELoader, VAEDecode, ImageBatchMulti, SaveImage, GetImageSizeAndCount, CLIPLoader, SetNode, SetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy showAnything, SetNode, easy anythingInversedSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CM_IntUnaryOperation, SimpleMath+, easy int, KSampler, PreviewImage, StringFunction|pysssss, easy positive, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextGenerateLTX2Prompt, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, GetNode, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, TextGenerateLTX2Prompt, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, GetImageSizeAndCount]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 483012602682833, "steps": 40, "width": 1024}
---

# 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Qwen-Image-2.1_2104076531101425666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（161 个）：
- `StringFunction|pysssss`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `easy saveText`
- `SetNode`
- `SetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `easy positive`
- `ImageLoader`
- `easy int`
- `SetNode`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `EmptyImage`
- `easy seed`
- `easy int`
- `easy int`
- `llama_cpp_parameters`
- `SetNode`
- `SetNode`
- `llama_cpp_model_loader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `VAEDecode` ★核心
- `ImageBatchMulti`
- `SaveImage`
- `GetImageSizeAndCount`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `easy anythingInversedSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_IntUnaryOperation`
- `SimpleMath+`
- `easy int`
- `KSampler` ★核心
- `PreviewImage`
- `StringFunction|pysssss`
- `easy positive`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `llama_cpp_instruct_adv`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `GetNode`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `483012602682833`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（66/161）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy positive`、`easy int`、`MemoryCleaner`、`EmptyImage`、`easy seed`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`UNETLoader`、`EmptyLatentImage`、`ImpactInt`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageBatchMulti`、`SaveImage`、`GetImageSizeAndCount`、`TextGenerateLTX2Prompt`、`easy anythingInversedSwitch`、`CM_IntUnaryOperation`、`SimpleMath+`、`KSampler`、`TextEncodeQwenImage21`、`llama_cpp_instruct_adv`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、easy seed
