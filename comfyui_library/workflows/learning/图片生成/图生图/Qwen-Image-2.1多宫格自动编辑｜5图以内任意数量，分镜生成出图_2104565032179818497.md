---
key: 图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json
name: Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json
hash: 7b141704fd8ecd6a
coverage: 0.522613
learned_at: 2026-10-21 00:43:18
nodes: [StringFunction|pysssss, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, easy saveText, SetNode, SetNode, Reroute, SetNode, easy int, SetNode, MemoryCleaner, EmptyImage, easy seed, llama_cpp_parameters, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, EmptyLatentImage, ImpactInt, ImpactInt, CLIPLoader, SetNode, VAELoader, VAEDecode, ImageBatchMulti, GetImageSizeAndCount, CLIPLoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy showAnything, SetNode, easy anythingInversedSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, TextEncodeQwenImage21, CM_IntUnaryOperation, SimpleMath+, KSampler, ImageLoader, ImageLoader, ImageLoader, ImageLoader, ImageLoader, easy positive, easy int, easy anythingIndexSwitch, ImageBatchMulti, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, easy positive, StringFunction|pysssss, ResolutionSelector, PreviewImage, GetNode, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, GetNode, llama_cpp_instruct_adv, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, llama_cpp_instruct_adv, GetNode, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextEncodeQwenImage21, SaveImage, GetImageSizeAndCount, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（199 个）：
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
- `Reroute`
- `SetNode`
- `easy int`
- `SetNode`
- `MemoryCleaner`
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **52%**（104/199）

**有卡**：`StringFunction|pysssss`、`ImageScaleToTotalPixels`、`easy saveText`、`easy int`、`MemoryCleaner`、`EmptyImage`、`easy seed`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`UNETLoader`、`EmptyLatentImage`、`ImpactInt`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageBatchMulti`、`GetImageSizeAndCount`、`TextEncodeQwenImage21`、`easy anythingInversedSwitch`、`CM_IntUnaryOperation`、`SimpleMath+`、`KSampler`、`ImageLoader`、`easy positive`、`easy anythingIndexSwitch`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`llama_cpp_instruct_adv`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
