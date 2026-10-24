---
key: 图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json
name: Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json
hash: 7fa5e65973ba83a9
coverage: 0.85
learned_at: 2026-10-23 11:13:22
nodes: [ModelSamplingAuraFlow, LayerMask: MaskGrow, VAEEncode, ImageConcanate, VAEDecode, KSampler, SaveImage, Note, ControlNetLoader, ControlNetInpaintingAliMamaApply, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, MarkdownNote, LoadImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 689602717979001, "steps": 10}
---

# 图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ModelSamplingAuraFlow`
- `LayerMask: MaskGrow`
- `VAEEncode` ★核心
- `ImageConcanate`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Note`
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `689602717979001`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`ModelSamplingAuraFlow`、`LayerMask: MaskGrow`、`VAEEncode`、`ImageConcanate`、`VAEDecode`、`KSampler`、`SaveImage`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
