---
key: 图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json
name: qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json
hash: 1972b4735b56c3e7
coverage: 0.876923
learned_at: 2026-10-21 02:57:26
nodes: [CLIPLoader, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, LoadImage, PrimitiveStringMultiline, ResolutionSelector, EmptyLatentImage, BatchImagesNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextGenerateLTX2Prompt, SamplerCustom, VAEDecode, SaveImage, KSamplerSelect, ManualSigmas, ComfySwitchNode, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfySwitchNode`
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

覆盖率 **88%**（57/65）

**有卡**：`CLIPLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`SamplerCustom`、`VAEDecode`、`SaveImage`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
