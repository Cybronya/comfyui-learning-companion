---
key: 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json
name: Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json
hash: dedd78a6f83e8532
coverage: 0.744681
learned_at: 2026-10-21 02:54:13
nodes: [VAEDecode, easy showAnything, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, SetNode, SetNode, CLIPLoader, VAELoader, Anything Everywhere3, AIO_Preprocessor, BatchImagesNode, GetNode, PreviewAny, EmptyLatentImage, Image Comparer (rgthree), GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, ResolutionSelector, EmptyLatentImage, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, VAEDecode, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, CLIPLoader, PreviewAny, CR Text Concatenate, Qwen3VL_Advanced, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, PreviewImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, CR Prompt Text, CLIPLoader, VAELoader, ComfySwitchNode, SaveImage, SaveImage, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree), LoadImage, ResolutionSelector, TextEncodeQwenImage21, LoraLoaderBypassModelOnly, KSampler, TextGenerateLTX2Prompt, KSampler, KSampler, CR Text, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `VAEDecode` ★核心
- `easy showAnything`
- `JjkText`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ComfySwitchNode`
- `GetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `AIO_Preprocessor`
- `BatchImagesNode`
- `GetNode`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PreviewAny`
- `CR Text Concatenate`
- `Qwen3VL_Advanced`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `ImageBlend`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `LoraLoaderBypassModelOnly` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `KSampler` ★核心
- `CR Text`
- `UNETLoader` ★核心
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **74%**（70/94）

**有卡**：`VAEDecode`、`SaveImage`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`AIO_Preprocessor`、`BatchImagesNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`LoadImage`、`CR Text Concatenate`、`Qwen3VL_Advanced`、`DWPreprocessor`、`DepthAnythingPreprocessor`、`ImageBlend`、`CR Prompt Text`、`LoraLoaderBypassModelOnly`、`KSampler`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
