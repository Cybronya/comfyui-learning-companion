---
key: 图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_1996091309645578242.json
name: 人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_1996091309645578242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_1996091309645578242.json
hash: 8be3580b4a05f552
coverage: 0.939394
learned_at: 2026-10-23 12:11:30
nodes: [ImageScaleToTotalPixels, DrawMaskOnImage, ImageResizeKJ, PreviewImage, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, SDPoseOODLoader, SDPoseOODProcessor, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LoadImage, ConditioningZeroOut, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, CFGNorm, VAEDecode, SeedVR2VideoUpscaler, SaveImage, ImageConcanate, ImageConcanate, PreviewImage, KSampler, LayerUtility: ImageBlend, easy imageRemBg, VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, BlockifyMask]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 790667075501092, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_1996091309645578242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物迁移替换qwen-image-edit 2511+seedvr2.5，香蕉全能图片V1pro平替_1996091309645578242.json`

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
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `BlockifyMask`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `790667075501092`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ImageScaleToTotalPixels`、`DrawMaskOnImage`、`ImageResizeKJ`、`ModelSamplingAuraFlow`、`LayerUtility: ImageScaleByAspectRatio V2`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`CLIPLoader`、`CFGNorm`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImageConcanate`、`KSampler`、`LayerUtility: ImageBlend`、`easy imageRemBg`、`VAEEncode`、`Int`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`BlockifyMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
