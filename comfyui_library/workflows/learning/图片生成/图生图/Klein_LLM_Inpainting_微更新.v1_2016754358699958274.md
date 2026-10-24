---
key: 图片生成/图生图/Klein_LLM_Inpainting_微更新.v1_2016754358699958274.json
name: Klein_LLM_Inpainting_微更新.v1_2016754358699958274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein_LLM_Inpainting_微更新.v1_2016754358699958274.json
hash: 7849b63b3ad7f617
coverage: 0.910714
learned_at: 2026-10-23 11:04:50
nodes: [Text Multiline, text-util-search-text, Text Multiline, CLIPLoader, VAELoader, easy saveText, ShowText|pysssss, ImageResizeKJv2, ImageAndMaskPreview, ColorMatch, INPAINT_ExpandMask, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, RandomNoise, SamplerCustomAdvanced, VAEDecode, Flux2Scheduler, KSamplerSelect, CFGGuider, ConditioningZeroOut, CLIPTextEncode, ReferenceLatent, ReferenceLatent, VAEEncode, InpaintModelConditioning, Fast Groups Muter (rgthree), PreviewAny, RH_LLMAPI_Pro_Node, Text Multiline, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, ConditioningZeroOut, CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, Text Concatenate, KSampler, Text Concatenate, UNETLoader, Note, ImageCompositeMasked, VAEDecode, Image Comparer (rgthree), SaveImage, MaskToImage, WA_ImageComposite, LoadImage, SaveImage, ImageConcatMulti, ImageConcatMulti, SaveImage, CustomAddLabel, Text Multiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 300542568218625, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Klein_LLM_Inpainting_微更新.v1_2016754358699958274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein_LLM_Inpainting_微更新.v1_2016754358699958274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `Text Multiline`
- `text-util-search-text`
- `Text Multiline`
- `CLIPLoader`
- `VAELoader`
- `easy saveText`
- `ShowText|pysssss`
- `ImageResizeKJv2`
- `ImageAndMaskPreview`
- `ColorMatch`
- `INPAINT_ExpandMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `InpaintModelConditioning`
- `Fast Groups Muter (rgthree)`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `Text Multiline`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `Text Concatenate`
- `KSampler` ★核心
- `Text Concatenate`
- `UNETLoader` ★核心
- `Note`
- `ImageCompositeMasked`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `MaskToImage`
- `WA_ImageComposite`
- `LoadImage`
- `SaveImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `CustomAddLabel`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `300542568218625`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（51/56）

**有卡**：`Text Multiline`、`text-util-search-text`、`CLIPLoader`、`VAELoader`、`easy saveText`、`ImageResizeKJv2`、`ImageAndMaskPreview`、`ColorMatch`、`INPAINT_ExpandMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`InpaintModelConditioning`、`RH_LLMAPI_Pro_Node`、`EmptyFlux2LatentImage`、`Text Concatenate`、`KSampler`、`ImageCompositeMasked`、`SaveImage`、`MaskToImage`、`WA_ImageComposite`、`LoadImage`、`ImageConcatMulti`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
