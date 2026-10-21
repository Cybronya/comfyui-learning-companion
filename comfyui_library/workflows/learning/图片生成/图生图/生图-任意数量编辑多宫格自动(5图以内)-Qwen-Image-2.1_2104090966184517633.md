---
key: 图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json
name: 生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json
hash: acd11c293011518b
coverage: 0.40625
learned_at: 2026-10-21 00:55:05
nodes: [StringFunction|pysssss, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, easy saveText, SetNode, SetNode, GetNode, Reroute, SetNode, easy int, SetNode, GetNode, MemoryCleaner, GetNode, EmptyImage, easy seed, llama_cpp_parameters, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, EmptyLatentImage, ImpactInt, ImpactInt, CLIPLoader, SetNode, VAELoader, VAEDecode, ImageBatchMulti, GetImageSizeAndCount, CLIPLoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy showAnything, SetNode, easy anythingInversedSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, TextEncodeQwenImage21, CM_IntUnaryOperation, SimpleMath+, KSampler, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageLoader, easy positive, easy int, easy anythingIndexSwitch, ImageBatchMulti, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, easy positive, StringFunction|pysssss, ResolutionSelector, PreviewImage, GetNode, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, GetNode, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextEncodeQwenImage21, SaveImage, GetImageSizeAndCount]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 324386800435644, "steps": 40, "width": 1024}
---

# 图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Qwen-Image-2.1_2104090966184517633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（160 个）：
- `StringFunction|pysssss`
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
- `easy int`
- `SetNode`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `EmptyImage`
- `easy seed`
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
- `GetImageSizeAndCount`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `SetNode`
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
- `ImageBatchMulti`
- `GetNode`
- `TextEncodeQwenImage21`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
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
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `CM_IntUnaryOperation`
- `SimpleMath+`
- `KSampler` ★核心
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `easy positive`
- `easy int`
- `easy anythingIndexSwitch`
- `ImageBatchMulti`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `easy positive`
- `StringFunction|pysssss`
- `ResolutionSelector`
- `PreviewImage`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `llama_cpp_instruct_adv`
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
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `SaveImage`
- `GetImageSizeAndCount`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `324386800435644`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（65/160）

**有卡**：`StringFunction|pysssss`、`ImageScaleToTotalPixels`、`easy saveText`、`easy int`、`MemoryCleaner`、`EmptyImage`、`easy seed`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`UNETLoader`、`EmptyLatentImage`、`ImpactInt`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageBatchMulti`、`GetImageSizeAndCount`、`TextEncodeQwenImage21`、`easy anythingInversedSwitch`、`CM_IntUnaryOperation`、`SimpleMath+`、`KSampler`、`ImageLoader`、`easy positive`、`easy anythingIndexSwitch`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`llama_cpp_instruct_adv`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
