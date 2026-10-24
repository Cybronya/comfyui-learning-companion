---
key: 图片生成/图生图/图生图-Qwen image- 扩图-Expand Image_2052553332648103938.json
name: 图生图-Qwen image- 扩图-Expand Image_2052553332648103938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图-Qwen image- 扩图-Expand Image_2052553332648103938.json
hash: 4bb9833ea7f78abc
coverage: 0.846154
learned_at: 2026-10-23 12:42:54
nodes: [KSampler, ControlNetInpaintingAliMamaApply, LoraLoaderModelOnly, CLIPTextEncode, MaskBlur+, ModelSamplingAuraFlow, Note, InvertMask, GrowMask, VAEEncode, SetLatentNoiseMask, MarkdownNote, Note, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Note, SaveImage, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, ControlNetLoader, LayerUtility: ExtendCanvasV2, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 3773001717150, "steps": 20}
---

# 图片生成/图生图/图生图-Qwen image- 扩图-Expand Image_2052553332648103938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图-Qwen image- 扩图-Expand Image_2052553332648103938.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `KSampler` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MaskBlur+`
- `ModelSamplingAuraFlow`
- `Note`
- `InvertMask`
- `GrowMask`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `MarkdownNote`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `LayerUtility: ExtendCanvasV2`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `3773001717150`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`KSampler`、`ControlNetInpaintingAliMamaApply`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`MaskBlur+`、`ModelSamplingAuraFlow`、`InvertMask`、`GrowMask`、`VAEEncode`、`SetLatentNoiseMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ControlNetLoader`、`LayerUtility: ExtendCanvasV2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
