---
key: 图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_2003766759352115202.json
name: 人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_2003766759352115202
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_2003766759352115202.json
hash: 59c16b2a980feef0
coverage: 0.939394
learned_at: 2026-10-23 12:11:31
nodes: [ImageScaleToTotalPixels, DrawMaskOnImage, ImageResizeKJ, PreviewImage, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, SDPoseOODLoader, SDPoseOODProcessor, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LoadImage, ConditioningZeroOut, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, CFGNorm, VAEDecode, SeedVR2VideoUpscaler, SaveImage, ImageConcanate, ImageConcanate, PreviewImage, KSampler, LayerUtility: ImageBlend, easy imageRemBg, VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, LoraLoaderModelOnly, PathchSageAttentionKJ, BlockifyMask, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 355280409389844, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_2003766759352115202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_2003766759352115202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ImageScaleToTotalPixels`
- `DrawMaskOnImage`
- `ImageResizeKJ`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CLIPLoader`
- `CFGNorm`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`
- `KSampler` ★核心
- `LayerUtility: ImageBlend`
- `easy imageRemBg`
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `BlockifyMask`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `355280409389844`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ImageScaleToTotalPixels`、`DrawMaskOnImage`、`ImageResizeKJ`、`ModelSamplingAuraFlow`、`LayerUtility: ImageScaleByAspectRatio V2`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`CLIPLoader`、`CFGNorm`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImageConcanate`、`KSampler`、`LayerUtility: ImageBlend`、`easy imageRemBg`、`VAEEncode`、`Int`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`BlockifyMask`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
