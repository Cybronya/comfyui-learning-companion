---
key: 图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json
name: Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json
hash: 9a40ca9029057a28
coverage: 0.88
learned_at: 2026-10-23 11:11:59
nodes: [ConditioningZeroOut, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, QwenEditConfigPreparer, LoraLoaderModelOnly, VAELoader, PreviewImage, ConditioningZeroOut, QwenEditOutputExtractor, QwenEditConfigPreparer, PreviewImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, QwenEditOutputExtractor, QwenEditConfigPreparer, PreviewImage, TextEncodeQwenImageEditPlusCustom_lrzjason, CheckpointLoaderSimple, LayerUtility: PurgeVRAM, PreviewImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, VAEDecode, CropWithPadInfo, PreviewImage, QwenEditAdaptiveLongestEdge, CropWithPadInfo, CropWithPadInfo, AddLabel, AddLabel, ImageScaleBy, QwenEditOutputExtractor, AddLabel, AddLabel, SaveImage, UNETLoader, CLIPLoader, SaveImage, LoadImage, ImageConcatMulti, PDIMAGE_LongerSize, SaveImage, SaveImage, PrimitiveStringMultiline, KSampler, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode` ★核心
- `QwenEditConfigPreparer`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PreviewImage`
- `ConditioningZeroOut`
- `QwenEditOutputExtractor`
- `QwenEditConfigPreparer`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `QwenEditConfigPreparer`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `PreviewImage`
- `QwenEditAdaptiveLongestEdge`
- `CropWithPadInfo`
- `CropWithPadInfo`
- `AddLabel`
- `AddLabel`
- `ImageScaleBy`
- `QwenEditOutputExtractor`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`VAEDecode`、`QwenEditConfigPreparer`、`LoraLoaderModelOnly`、`VAELoader`、`QwenEditOutputExtractor`、`UNETLoader`、`KSampler`、`CheckpointLoaderSimple`、`LayerUtility: PurgeVRAM`、`CropWithPadInfo`、`QwenEditAdaptiveLongestEdge`、`AddLabel`、`ImageScaleBy`、`SaveImage`、`CLIPLoader`、`LoadImage`、`ImageConcatMulti`、`PDIMAGE_LongerSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
