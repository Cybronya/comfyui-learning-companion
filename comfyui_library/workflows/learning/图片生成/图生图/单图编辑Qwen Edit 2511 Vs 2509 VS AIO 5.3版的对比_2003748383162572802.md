---
key: 图片生成/图生图/单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802.json
name: 单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802.json
hash: fba92893179b5876
coverage: 0.836735
learned_at: 2026-10-23 12:32:29
nodes: [ImageScaleBy, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, ConditioningZeroOut, KSampler, QwenEditOutputExtractor, VAEDecode, PreviewImage, LayerUtility: PurgeVRAM, AddLabel, CropWithPadInfo, VAELoader, UNETLoader, TextEncodeQwenImageEditPlusCustom_lrzjason, LoraLoaderModelOnly, VAEDecode, QwenEditOutputExtractor, KSampler, ConditioningZeroOut, PreviewImage, CropWithPadInfo, AddLabel, UNETLoader, LoraLoaderModelOnly, CLIPLoader, QwenEditConfigPreparer, CheckpointLoaderSimple, ConditioningZeroOut, PreviewImage, KSampler, VAEDecode, CropWithPadInfo, LayerUtility: PurgeVRAM, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditOutputExtractor, PDIMAGE_LongerSize, LayerUtility: PurgeVRAM, PreviewImage, PreviewImage, AddLabel, ImageConcatMulti, AddLabel, QwenEditAdaptiveLongestEdge, SaveImage, LoadImage, MarkdownNote, QwenEditConfigPreparer, PreviewImage, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `ImageScaleBy`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `CropWithPadInfo`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `QwenEditOutputExtractor`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `CropWithPadInfo`
- `AddLabel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `QwenEditConfigPreparer`
- `CheckpointLoaderSimple` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditOutputExtractor`
- `PDIMAGE_LongerSize`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `PreviewImage`
- `AddLabel`
- `ImageConcatMulti`
- `AddLabel`
- `QwenEditAdaptiveLongestEdge`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `QwenEditConfigPreparer`
- `PreviewImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **84%**（41/49）

**有卡**：`ImageScaleBy`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`ConditioningZeroOut`、`KSampler`、`QwenEditOutputExtractor`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`AddLabel`、`CropWithPadInfo`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`CheckpointLoaderSimple`、`PDIMAGE_LongerSize`、`ImageConcatMulti`、`QwenEditAdaptiveLongestEdge`、`SaveImage`、`LoadImage`

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
