---
key: 图片生成/图生图/免费开源 flux kontext dev多图融合 三图编辑-LLM智能扩写 一句修改图-StarA_1938532546777145346.json
name: 免费开源 flux kontext dev多图融合 三图编辑-LLM智能扩写 一句修改图-StarA_1938532546777145346
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/免费开源 flux kontext dev多图融合 三图编辑-LLM智能扩写 一句修改图-StarA_1938532546777145346.json
hash: d13972c5299cf36f
coverage: 0.888889
learned_at: 2026-10-23 12:13:06
nodes: [Note Plus (mtb), ModelSamplingFlux, VAELoader, DualCLIPLoader, VAEEncode, ReferenceLatent, EmptyLatentImage, ConditioningZeroOut, KSampler, VAEDecode, FluxGuidance, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SaveImage, FluxResolutionNode, PreviewImage, PreviewImage, RMBG, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, ImageResize+, RMBG, LoadImage, LoadImage, PreviewImage, LoadImage, MarkdownNote, RH_LLMAPI_NODE, CLIPTextEncode, NunchakuFluxDiTLoader, Text]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 956821485565212, "steps": 20, "width": 1024}
---

# 图片生成/图生图/免费开源 flux kontext dev多图融合 三图编辑-LLM智能扩写 一句修改图-StarA_1938532546777145346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/免费开源 flux kontext dev多图融合 三图编辑-LLM智能扩写 一句修改图-StarA_1938532546777145346.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Note Plus (mtb)`
- `ModelSamplingFlux`
- `VAELoader`
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `FluxResolutionNode`
- `PreviewImage`
- `PreviewImage`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `ImageResize+`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `Text`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `956821485565212`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`Note Plus (mtb)`、`ModelSamplingFlux`、`VAELoader`、`DualCLIPLoader`、`VAEEncode`、`ReferenceLatent`、`EmptyLatentImage`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`FluxGuidance`、`MathExpression|pysssss`、`SaveImage`、`FluxResolutionNode`、`RMBG`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageRemoveAlpha`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadImage`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`NunchakuFluxDiTLoader`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
