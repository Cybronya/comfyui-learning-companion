---
key: 图片生成/文生图/Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993.json
name: Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993.json
hash: b8dda1d637262dad
coverage: 0.777778
learned_at: 2026-10-19 22:00:43
nodes: [UNETLoader, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditOutputExtractor, SetNode, GetNode, GetNode, QwenEditConfigPreparer, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, KSampler, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlusCustom_lrzjason, GetNode, GetNode, QwenEditConfigPreparer, LayerUtility: PurgeVRAM, KSampler, LoraLoaderModelOnly, UNETLoader, QwenEditOutputExtractor, ConditioningZeroOut, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, GetNode, CheckpointLoaderSimple, VAEDecode, LayerUtility: PurgeVRAM, LoadImage, CropWithPadInfo, QwenEditOutputExtractor, CropWithPadInfo, CropWithPadInfo, ImageScaleBy, Anything Everywhere3, CLIPLoader, VAELoader, SetNode, PreviewImage, PreviewImage, PreviewImage, CR Text, KSampler, QwenEditAdaptiveLongestEdge, PDIMAGE_LongerSize, ImageConcatMulti, SaveImage, AddLabel, AddLabel, AddLabel, AddLabel, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditOutputExtractor`
- `SetNode`
- `GetNode`
- `GetNode`
- `QwenEditConfigPreparer`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `GetNode`
- `GetNode`
- `QwenEditConfigPreparer`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `QwenEditOutputExtractor`
- `ConditioningZeroOut`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `CropWithPadInfo`
- `QwenEditOutputExtractor`
- `CropWithPadInfo`
- `CropWithPadInfo`
- `ImageScaleBy`
- `Anything Everywhere3`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CR Text`
- `KSampler` ★核心
- `QwenEditAdaptiveLongestEdge`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`VAEDecode`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditOutputExtractor`、`QwenEditConfigPreparer`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`KSampler`、`CheckpointLoaderSimple`、`LoadImage`、`CropWithPadInfo`、`ImageScaleBy`、`CLIPLoader`、`VAELoader`、`CR Text`、`QwenEditAdaptiveLongestEdge`、`PDIMAGE_LongerSize`、`ImageConcatMulti`、`SaveImage`、`AddLabel`

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
