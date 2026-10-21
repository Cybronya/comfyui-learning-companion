---
key: 图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json
name: 人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json
hash: ab75374df380b196
coverage: 0.833333
learned_at: 2026-10-21 00:47:57
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEEncode, ReferenceLatent, ConditioningZeroOut, RH_Captioner, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, ModelSamplingAuraFlow, RunningHub Deepcleaner, LoraLoaderModelOnly, LatentUpscaleBy, VAEDecode, VAEDecode, KSamplerAdvanced, ColorMatch, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, workflow>高清节点, SaveImage, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), ImageScaleBy, Image Comparer (rgthree), Image Comparer (rgthree), Note, CLIPTextEncode, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 756645278950561, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人像超高清修复Ultra-High-Definition_Portrait_Retouching,_2099671450700570625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `RH_Captioner`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `RunningHub Deepcleaner`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleBy`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ColorMatch`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SaveImage`
- `workflow>高清节点`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `756645278950561`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`RH_Captioner`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`RunningHub Deepcleaner`、`LoraLoaderModelOnly`、`LatentUpscaleBy`、`VAEDecode`、`KSamplerAdvanced`、`ColorMatch`、`KSampler`、`SaveImage`、`workflow>高清节点`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleBy`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
