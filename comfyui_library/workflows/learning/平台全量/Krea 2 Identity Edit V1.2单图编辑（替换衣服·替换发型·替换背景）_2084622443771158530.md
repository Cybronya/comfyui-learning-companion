---
key: 平台全量/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2084622443771158530.json
name: Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2084622443771158530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2084622443771158530.json
hash: 3175bd5ce49c1d5e
coverage: 0.882353
learned_at: 2026-11-14 00:36:05
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, FluxKontextImageScale, FluxKontextImageScale, Krea2EditGroundedEncode, LayerUtility: ImageScaleByAspectRatio V2, Krea2EditModelPatch, VAEEncode, Krea2EditGroundedEncode, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, KSampler, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 455334805099258, "steps": 11}
---

# 平台全量/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2084622443771158530.json

> 来源文件 `comfyui_library/workflows/平台全量/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2084622443771158530.json`

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

- `seed` = `455334805099258`
- `steps` = `11`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`FluxKontextImageScale`、`Krea2EditGroundedEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Krea2EditModelPatch`、`VAEEncode`、`VAEDecode`、`SaveImage`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、Krea2EditGroundedEncode
