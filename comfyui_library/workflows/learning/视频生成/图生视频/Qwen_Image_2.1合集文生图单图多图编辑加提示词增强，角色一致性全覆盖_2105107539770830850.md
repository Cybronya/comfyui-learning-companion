---
key: 视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json
name: Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json
hash: 970dd3b1bf87cf5a
coverage: 0.526316
learned_at: 2026-10-17 22:18:55
nodes: [SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LoadImage, LoadImage, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, BatchImagesNode, GetNode, LoadImage, GetNode, EmptyLatentImage, PreviewAny, ComfySwitchNode, QwenImage21Cache, PrimitiveInt, UNETLoader, TextEncodeQwenImage21, ResolutionSelector, SetNode, easy seed, GetNode, LoadImage, LoadImage, PrimitiveBoolean, VAEDecode, SetNode, GetNode, SetNode, CLIPLoader, GetNode, GetNode, TextGenerateLTX2Prompt, KSampler, SaveImageAdvanced, SetNode, SetNode, CLIPLoader, CLIPLoader, JjkText, SetNode, SetNode, SetNode, SetNode, ResolutionSelector, PrimitiveBoolean, GetNode, GetNode, EmptyLatentImage, SetNode, easy seed, JjkText, GetNode, GetNode, GetNode, easy showAnything, TextGenerateLTX2Prompt, GetNode, TextEncodeQwenImage21, GetNode, VAEDecode, KSampler, SetNode, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `BatchImagesNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `SetNode`
- `easy seed`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `JjkText`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `easy seed`
- `JjkText`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **53%**（70/133）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VAELoader`、`BatchImagesNode`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`easy seed`、`PrimitiveBoolean`、`VAEDecode`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
