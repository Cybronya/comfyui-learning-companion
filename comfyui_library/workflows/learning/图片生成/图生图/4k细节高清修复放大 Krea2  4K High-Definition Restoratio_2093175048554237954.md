---
key: 图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json
name: 4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json
hash: 32f1fdb25d0db35a
coverage: 0.916667
learned_at: 2026-10-21 00:38:30
nodes: [ConditioningZeroOut, ImageScaleToTotalPixels, PrimitiveFloat, FluxKVCache, easy cleanGpuUsed, Anything Everywhere3, LoraLoaderModelOnly, UpscaleModelLoader, ReferenceLatent, KSampler, VAEEncodeTiled, LoraLoaderModelOnly, GetImageSize, ConditioningZeroOut, VAEEncode, ConditioningZeroOut, Flux2KleinModelConfig_EditUtils, ReferenceLatent, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, KSamplerSelect, CFGGuider, RandomNoise, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageUpscaleWithModel, Flux2KleinConfigPreparer_EditUtils, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, VAEDecode, Image Comparer (rgthree), VAEDecodeTiled, easy imageColorMatch, easy imageColorMatch, CLIPTextEncode, EditTextEncode_EditUtils, CLIPTextEncode, VAELoader, CLIPLoader, UNETLoader, LoadImage, Note, LatentColorMatchSimple, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "euler_ancestral", "scheduler": "kl_optimal", "seed": 384645269526357, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `PrimitiveFloat`
- `FluxKVCache`
- `easy cleanGpuUsed`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `ReferenceLatent`
- `KSampler` ★核心
- `VAEEncodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `Flux2KleinModelConfig_EditUtils`
- `ReferenceLatent`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageUpscaleWithModel`
- `Flux2KleinConfigPreparer_EditUtils`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecodeTiled` ★核心
- `easy imageColorMatch`
- `easy imageColorMatch`
- `CLIPTextEncode` ★核心
- `EditTextEncode_EditUtils`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `Note`
- `LatentColorMatchSimple`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `384645269526357`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `kl_optimal`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`FluxKVCache`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`ReferenceLatent`、`KSampler`、`VAEEncodeTiled`、`GetImageSize`、`VAEEncode`、`Flux2KleinModelConfig_EditUtils`、`Flux2KleinOutputExtractor_EditUtils`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`ImageUpscaleWithModel`、`Flux2KleinConfigPreparer_EditUtils`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeTiled`、`easy imageColorMatch`、`CLIPTextEncode`、`EditTextEncode_EditUtils`、`LoadImage`、`LatentColorMatchSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
