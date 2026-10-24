---
key: 图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json
name: F.2klein9b电商产品主图匹配融合场景_2053459372717690881
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json
hash: 318d8997dfb3b535
coverage: 0.829787
learned_at: 2026-10-23 10:52:52
nodes: [KSamplerSelect, BasicGuider, Flux2Scheduler, EmptyLatentImage, ReferenceLatent, VAEEncode, CLIPTextEncode, ReferenceLatent, easy cleanGpuUsed, RandomNoise, CLIPLoader, UNETLoader, PrimitiveNode, easy ifElse, easy isMaskEmpty, LaMaInpainting, easy ifElse, ImageToMask, VAEEncode, ImageConcatMulti, FluxKontextImageScale, FluxKontextImageScale, VAELoader, KSampler, ReferenceLatent, VAEEncode, VAEDecode, GetImageSize, easy positive, PainterFluxImageEdit, CR Text, Note, SaveImage, SamplerCustomAdvanced, VAEDecode, PreviewImage, RMBG, FluxKontextImageScale, Image Comparer (rgthree), LoadImage, LoadImage, PreviewAny, Int, PreviewImage, AILab_QwenVL, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 787064676985703, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `Flux2Scheduler`
- `EmptyLatentImage` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `easy cleanGpuUsed`
- `RandomNoise`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `easy ifElse`
- `easy isMaskEmpty`
- `LaMaInpainting`
- `easy ifElse`
- `ImageToMask`
- `VAEEncode` ★核心
- `ImageConcatMulti`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `VAELoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `easy positive`
- `PainterFluxImageEdit`
- `CR Text`
- `Note`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `RMBG`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `Int`
- `PreviewImage`
- `AILab_QwenVL`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `787064676985703`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`KSamplerSelect`、`BasicGuider`、`Flux2Scheduler`、`EmptyLatentImage`、`ReferenceLatent`、`VAEEncode`、`CLIPTextEncode`、`easy cleanGpuUsed`、`RandomNoise`、`CLIPLoader`、`UNETLoader`、`easy isMaskEmpty`、`LaMaInpainting`、`ImageToMask`、`ImageConcatMulti`、`FluxKontextImageScale`、`VAELoader`、`KSampler`、`VAEDecode`、`GetImageSize`、`easy positive`、`PainterFluxImageEdit`、`CR Text`、`SaveImage`、`SamplerCustomAdvanced`、`RMBG`、`LoadImage`、`Int`、`AILab_QwenVL`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
