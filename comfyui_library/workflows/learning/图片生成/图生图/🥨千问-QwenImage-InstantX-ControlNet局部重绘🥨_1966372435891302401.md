---
key: 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json
name: 🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json
hash: ab80c5e10fd48b6b
coverage: 0.818182
learned_at: 2026-10-23 13:40:22
nodes: [ModelSamplingAuraFlow, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, ControlNetInpaintingAliMamaApply, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskGrow, VAEEncode, Note, ImageConcanate, VAEDecode, KSampler, PreviewImage, SaveImage, MarkdownNote, Note Plus (mtb), LoadImage, LoraLoaderModelOnly, ControlNetLoader, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 293881042541481, "steps": 10}
---

# 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ControlNetInpaintingAliMamaApply`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskGrow`
- `VAEEncode` ★核心
- `Note`
- `ImageConcanate`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `293881042541481`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`ControlNetInpaintingAliMamaApply`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskGrow`、`VAEEncode`、`ImageConcanate`、`VAEDecode`、`KSampler`、`SaveImage`、`Note Plus (mtb)`、`LoadImage`、`LoraLoaderModelOnly`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
