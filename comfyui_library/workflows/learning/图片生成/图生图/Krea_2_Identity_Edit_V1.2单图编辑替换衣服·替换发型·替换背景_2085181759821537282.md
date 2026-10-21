---
key: 图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282.json
name: Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282.json
hash: a9fa6ba945e8ffa2
coverage: 0.882353
learned_at: 2026-10-21 00:41:27
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, FluxKontextImageScale, FluxKontextImageScale, Krea2EditGroundedEncode, LayerUtility: ImageScaleByAspectRatio V2, Krea2EditModelPatch, VAEEncode, Krea2EditGroundedEncode, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, KSampler, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 741622666827793, "steps": 11}
---

# 图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `Krea2EditGroundedEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Krea2EditModelPatch`
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `KSampler` ★核心
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `741622666827793`
- `steps` = `11`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`FluxKontextImageScale`、`Krea2EditGroundedEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Krea2EditModelPatch`、`VAEEncode`、`VAEDecode`、`SaveImage`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、VAEEncode
