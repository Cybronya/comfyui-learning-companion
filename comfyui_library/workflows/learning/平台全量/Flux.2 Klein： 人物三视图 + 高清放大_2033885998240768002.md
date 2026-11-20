---
key: 平台全量/Flux.2 Klein： 人物三视图 + 高清放大_2033885998240768002.json
name: Flux.2 Klein： 人物三视图 + 高清放大_2033885998240768002
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 Klein： 人物三视图 + 高清放大_2033885998240768002.json
hash: 5c55817468ad0f5e
coverage: 0.864865
learned_at: 2026-11-14 00:28:52
nodes: [VAEEncode, VAEEncode, CLIPTextEncode, CLIPTextEncode, RMBG, PreviewImage, KSampler, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, LatentUpscaleBy, CLIPTextEncode, ReferenceLatent, CLIPTextEncode, ReferenceLatent, KSampler, VAEDecode, UNETLoader, easy positive, LoadImage, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, Note, Image Comparer (rgthree), VAEDecode, SaveImage, LayerColor: ColorAdapter, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, SeedVR2VideoUpscaler, PreviewImage, Image Comparer (rgthree), LayerUtility: PurgeVRAM]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 672845050069827, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 Klein： 人物三视图 + 高清放大_2033885998240768002.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 Klein： 人物三视图 + 高清放大_2033885998240768002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RMBG`
- `PreviewImage`
- `KSampler` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `LatentUpscaleBy`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `easy positive`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `Note`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerColor: ColorAdapter`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `672845050069827`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`VAEEncode`、`CLIPTextEncode`、`RMBG`、`KSampler`、`ReferenceLatent`、`CLIPLoader`、`VAELoader`、`LatentUpscaleBy`、`VAEDecode`、`UNETLoader`、`easy positive`、`LoadImage`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`SaveImage`、`LayerColor: ColorAdapter`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、SeedVR2LoadDiTModel

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
