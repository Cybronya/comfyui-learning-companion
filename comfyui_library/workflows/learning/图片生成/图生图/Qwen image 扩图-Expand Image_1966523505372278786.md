---
key: 图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json
name: Qwen image 扩图-Expand Image_1966523505372278786
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json
hash: 6ca55f1804f6cb46
coverage: 0.785714
learned_at: 2026-10-23 11:14:18
nodes: [KSampler, ControlNetInpaintingAliMamaApply, LoraLoaderModelOnly, MarkdownNote, CLIPTextEncode, MaskBlur+, ModelSamplingAuraFlow, Note, InvertMask, GrowMask, VAEEncode, SetLatentNoiseMask, MarkdownNote, Note, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Note, SaveImage, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, ControlNetLoader, LoadImage, LayerUtility: ExtendCanvasV2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 711233733835106, "steps": 20}
---

# 图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `KSampler` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
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
- `MarkdownNote`
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
- `LoadImage`
- `LayerUtility: ExtendCanvasV2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `711233733835106`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`KSampler`、`ControlNetInpaintingAliMamaApply`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`MaskBlur+`、`ModelSamplingAuraFlow`、`InvertMask`、`GrowMask`、`VAEEncode`、`SetLatentNoiseMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ControlNetLoader`、`LoadImage`、`LayerUtility: ExtendCanvasV2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
