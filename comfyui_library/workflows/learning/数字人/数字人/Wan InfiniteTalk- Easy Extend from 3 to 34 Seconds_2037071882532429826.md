---
key: 数字人/数字人/Wan InfiniteTalk- Easy Extend from 3 to 34 Seconds_2037071882532429826.json
name: Wan InfiniteTalk- Easy Extend from 3 to 34 Seconds_2037071882532429826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan InfiniteTalk- Easy Extend from 3 to 34 Seconds_2037071882532429826.json
hash: c07eb683578251f1
coverage: 0.95082
learned_at: 2026-10-26 01:57:43
nodes: [ConditioningZeroOut, WanInfiniteTalkToVideo, CLIPTextEncode, AudioEncoderEncode, MarkdownNote, VAEDecode, KSampler, WanInfiniteTalkToVideo, KSampler, VAEDecode, ImageFromBatch, KSampler, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, BatchImagesNode, VAEDecode, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, BatchImagesNode, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, KSampler, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, BatchImagesNode, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, BatchImagesNode, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, BatchImagesNode, VAEDecode, ImageFromBatch, WanInfiniteTalkToVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, KSampler, KSampler, KSampler, KSampler, KSampler, BatchImagesNode, VAEDecode, ImageFromBatch, VHS_VideoCombine, KSampler, WanInfiniteTalkToVideo, VAEDecode, ImageFromBatch, VHS_VideoCombine, KSampler, WanInfiniteTalkToVideo, BatchImagesNode, ImageFromBatch, BatchImagesNode, VHS_VideoCombine, KSampler, WanInfiniteTalkToVideo, BatchImagesNode, BatchImagesNode, BatchImagesNode, WanInfiniteTalkToVideo, Node Collector (rgthree), Node Collector (rgthree), Node Collector (rgthree), Node Collector (rgthree), Node Collector (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Node Collector (rgthree), Node Collector (rgthree), Mute / Bypass Repeater (rgthree), Node Collector (rgthree), Node Collector (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Node Collector (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Node Collector (rgthree), Node Collector (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), UNETLoader, LoraLoaderModelOnly, ModelPatchLoader, AudioEncoderLoader, CLIPLoader, MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, VAELoader, LoadImage, VHS_LoadAudioUpload, VAEDecode, VHS_VideoCombine, MarkdownNote, VHS_VideoCombine, Fast Muter (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 474638617657772, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Wan InfiniteTalk- Easy Extend from 3 to 34 Seconds_2037071882532429826.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan InfiniteTalk- Easy Extend from 3 to 34 Seconds_2037071882532429826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（122 个）：
- `ConditioningZeroOut`
- `WanInfiniteTalkToVideo`
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `MarkdownNote`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `BatchImagesNode`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `ImageFromBatch`
- `BatchImagesNode`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `BatchImagesNode`
- `BatchImagesNode`
- `BatchImagesNode`
- `WanInfiniteTalkToVideo`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Node Collector (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Node Collector (rgthree)`
- `Node Collector (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAELoader`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `VHS_VideoCombine`
- `Fast Muter (rgthree)`

## 关键参数

- `seed` = `474638617657772`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **95%**（116/122）

**有卡**：`ConditioningZeroOut`、`WanInfiniteTalkToVideo`、`CLIPTextEncode`、`AudioEncoderEncode`、`VAEDecode`、`KSampler`、`ImageFromBatch`、`BatchImagesNode`、`VHS_VideoCombine`、`Node Collector (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`AudioEncoderLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_LoadAudioUpload`、`Fast Muter (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 12 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
