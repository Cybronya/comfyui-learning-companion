---
key: 图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json
name: Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json
hash: 55066b5e9427e07c
coverage: 0.478947
learned_at: 2026-10-21 00:42:20
nodes: [StringFunction|pysssss, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, easy saveText, SetNode, SetNode, GetNode, Reroute, SetNode, easy positive, ImageLoader, easy int, SetNode, GetNode, MemoryCleaner, GetNode, EmptyImage, easy seed, easy int, easy int, llama_cpp_parameters, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, EmptyLatentImage, ImpactInt, ImpactInt, CLIPLoader, SetNode, VAELoader, VAEDecode, ImageBatchMulti, SaveImage, GetImageSizeAndCount, CLIPLoader, SetNode, SetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy showAnything, SetNode, easy anythingInversedSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CM_IntUnaryOperation, SimpleMath+, easy int, KSampler, PreviewImage, StringFunction|pysssss, easy positive, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, TextGenerateLTX2Prompt, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, GetNode, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, TextGenerateLTX2Prompt, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, GetImageSizeAndCount, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（190 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **48%**（91/190）

**有卡**：`StringFunction|pysssss`、`ImageLoader`、`ImageScaleToTotalPixels`、`easy saveText`、`easy positive`、`easy int`、`MemoryCleaner`、`EmptyImage`、`easy seed`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`UNETLoader`、`EmptyLatentImage`、`ImpactInt`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageBatchMulti`、`SaveImage`、`GetImageSizeAndCount`、`TextGenerateLTX2Prompt`、`easy anythingInversedSwitch`、`CM_IntUnaryOperation`、`SimpleMath+`、`KSampler`、`TextEncodeQwenImage21`、`llama_cpp_instruct_adv`、`easy anythingIndexSwitch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
