---
key: 平台全量/【电商产品打光合成】F.1Kontext电商产品 重新打光 万物光影融合全能溶图产品打光合成换背景__1980885008590225409.json
name: 【电商产品打光合成】F.1Kontext电商产品 重新打光 万物光影融合全能溶图产品打光合成换背景__1980885008590225409
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【电商产品打光合成】F.1Kontext电商产品 重新打光 万物光影融合全能溶图产品打光合成换背景__1980885008590225409.json
hash: 5db9731a706ed5c7
coverage: 0.818182
learned_at: 2026-11-14 01:24:42
nodes: [VAELoader, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, PreviewImage, Fast Groups Bypasser (rgthree), CLIPTextEncode, RH_Translator, UNETLoader, DualCLIPLoader, VAEDecode, ReferenceLatent, FluxGuidance, VAEEncode, ConditioningZeroOut, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, KSampler, SaveImage, LoraLoaderModelOnly, SUPIR_Upscale, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 457212036731313, "steps": 30}
---

# 平台全量/【电商产品打光合成】F.1Kontext电商产品 重新打光 万物光影融合全能溶图产品打光合成换背景__1980885008590225409.json

> 来源文件 `comfyui_library/workflows/平台全量/【电商产品打光合成】F.1Kontext电商产品 重新打光 万物光影融合全能溶图产品打光合成换背景__1980885008590225409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `SUPIR_Upscale`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `457212036731313`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`VAELoader`、`LoadImage`、`CLIPTextEncode`、`RH_Translator`、`UNETLoader`、`DualCLIPLoader`、`VAEDecode`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`、`SUPIR_Upscale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
