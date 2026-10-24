---
key: 图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json
name: Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json
hash: 9b8854f22a2614c9
coverage: 0.882353
learned_at: 2026-10-23 11:07:34
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecode, Krea2EditGroundedEncode, Krea2EditGroundedEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, Krea2EditModelPatch, MarkdownNote, SaveImage, FluxKontextImageScale, VAEEncode, FluxKontextImageScale, LoadImage, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 418351351616892, "steps": 10}
---

# 图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Krea2EditModelPatch`
- `MarkdownNote`
- `SaveImage`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `LoadImage`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `418351351616892`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`Krea2EditGroundedEncode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`Krea2EditModelPatch`、`SaveImage`、`FluxKontextImageScale`、`VAEEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、VAEEncode
