---
key: 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json
name: 🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json
hash: 81df3487674292dd
coverage: 0.851852
learned_at: 2026-10-23 13:40:21
nodes: [ModelSamplingAuraFlow, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, ControlNetInpaintingAliMamaApply, Note, ImageConcanate, VAEDecode, SaveImage, MarkdownNote, Note Plus (mtb), CLIPTextEncode, PreviewImage, VAEEncode, KSampler, MarkdownNote, LoadImage, LoraLoaderModelOnly, GrowMaskWithBlur, PurgeVRAM_UTK, PurgeVRAM_UTK, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, PurgeVRAM_UTK, PurgeVRAM_UTK, ImagePadForOutpaint]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 480951066122955, "steps": 10}
---

# 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ControlNetInpaintingAliMamaApply`
- `Note`
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `Note Plus (mtb)`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `GrowMaskWithBlur`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `ImagePadForOutpaint`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `480951066122955`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`ControlNetInpaintingAliMamaApply`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`Note Plus (mtb)`、`VAEEncode`、`KSampler`、`LoadImage`、`LoraLoaderModelOnly`、`GrowMaskWithBlur`、`PurgeVRAM_UTK`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
