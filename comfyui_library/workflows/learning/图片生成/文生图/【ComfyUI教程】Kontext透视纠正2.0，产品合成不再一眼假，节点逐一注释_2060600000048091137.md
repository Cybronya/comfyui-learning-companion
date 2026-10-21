---
key: 图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json
name: 【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json
hash: c9c6bb6acfeda7c4
coverage: 0.529412
learned_at: 2026-10-19 23:03:34
nodes: [CLIPTextEncode, KSampler, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, FluxGuidance, ImpactInt, ReferenceLatent, LayerUtility: ImageMaskScaleAs, VAEDecode, LoraLoaderModelOnly, DualCLIPLoader, LoraLoaderModelOnly, UNETLoader, LoadImage, SaveImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 472570843917866, "steps": 30}
---

# 图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `FluxGuidance`
- `ImpactInt`
- `ReferenceLatent`
- `LayerUtility: ImageMaskScaleAs`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `472570843917866`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **53%**（18/34）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`FluxGuidance`、`ImpactInt`、`ReferenceLatent`、`LayerUtility: ImageMaskScaleAs`、`VAEDecode`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
