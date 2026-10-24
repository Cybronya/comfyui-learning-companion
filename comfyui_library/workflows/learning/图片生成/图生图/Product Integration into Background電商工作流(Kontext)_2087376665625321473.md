---
key: 图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json
name: Product Integration into Background電商工作流(Kontext)_2087376665625321473
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json
hash: 58ac3a04da974f7e
coverage: 0.896552
learned_at: 2026-10-23 11:10:54
nodes: [VAELoader, DualCLIPLoader, UNETLoader, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, KSampler, ReferenceLatent, FluxGuidance, ConditioningZeroOut, LayerUtility: FluxKontextImageScale, LayerUtility: AnyRerouter, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, InspyrenetRembg, FastCanvasTool, VAEDecode, CLIPTextEncode, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, LoadImage, Note, VAEEncode, LayerUtility: HLFrequencyDetailRestore, PMRF, SaveImage, Note, LoadImage, FastCanvas]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 519115423063091, "steps": 20}
---

# 图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `KSampler` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `LayerUtility: FluxKontextImageScale`
- `LayerUtility: AnyRerouter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InspyrenetRembg`
- `FastCanvasTool`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Note`
- `VAEEncode` ★核心
- `LayerUtility: HLFrequencyDetailRestore`
- `PMRF`
- `SaveImage`
- `Note`
- `LoadImage`
- `FastCanvas`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `519115423063091`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`LayerMask: MaskGrow`、`LayerUtility: ImageMaskScaleAs`、`KSampler`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`LayerUtility: FluxKontextImageScale`、`LayerUtility: AnyRerouter`、`LayerUtility: ImageScaleByAspectRatio V2`、`InspyrenetRembg`、`FastCanvasTool`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`VAEEncode`、`LayerUtility: HLFrequencyDetailRestore`、`PMRF`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
