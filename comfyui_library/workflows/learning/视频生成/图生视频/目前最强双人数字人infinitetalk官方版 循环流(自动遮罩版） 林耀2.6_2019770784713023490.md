---
key: 视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json
name: 目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019770784713023490.json
hash: 56e7714acbfa09cd
coverage: 0.745098
learned_at: 2026-10-15 22:35:04
nodes: [CLIPLoader, Reroute, Reroute, LoraLoaderModelOnly, Reroute, Reroute, VAEDecode, ConditioningZeroOut, MarkdownNote, Reroute, AudioEncoderLoader, KSampler, KSampler, VAEDecode, ModelPatchLoader, easy forLoopStart, VAELoader, MaskPreview, MaskPreview, MaskPreview, ImageBatch, Reroute, Reroute, AudioEncoderEncode, AudioEncoderEncode, Reroute, Reroute, ImageFromBatch, Reroute, WanInfiniteTalkToVideo, LoadAudio, LoadAudio, WanInfiniteTalkToVideo, UNETLoader, CreateVideo, PrimitiveInt, CLIPTextEncode, PrimitiveInt, SimpleCalculatorKJ, Audio Duration (mtb), AudioConcat, LoadImage, SegmentV2, easy forLoopEnd, VHS_VideoCombine, SaveVideo, ZML_MaskSeparateDistance, JWInteger, PreviewAudio, ShowAnything|Mie, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1051398958351444, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/目前最强双人数字人infinitetalk官方版 循环流(自动遮罩版） 林耀2.6_2019770784713023490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019770784713023490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `Reroute`
- `AudioEncoderLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelPatchLoader`
- `easy forLoopStart`
- `VAELoader`
- `MaskPreview`
- `MaskPreview`
- `MaskPreview`
- `ImageBatch`
- `Reroute`
- `Reroute`
- `AudioEncoderEncode`
- `AudioEncoderEncode`
- `Reroute`
- `Reroute`
- `ImageFromBatch`
- `Reroute`
- `WanInfiniteTalkToVideo`
- `LoadAudio`
- `LoadAudio`
- `WanInfiniteTalkToVideo`
- `UNETLoader` ★核心
- `CreateVideo`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `SimpleCalculatorKJ`
- `Audio Duration (mtb)`
- `AudioConcat`
- `LoadImage`
- `SegmentV2`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `SaveVideo`
- `ZML_MaskSeparateDistance`
- `JWInteger`
- `PreviewAudio`
- `ShowAnything|Mie`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `1051398958351444`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **75%**（38/51）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ConditioningZeroOut`、`AudioEncoderLoader`、`KSampler`、`ModelPatchLoader`、`easy forLoopStart`、`VAELoader`、`MaskPreview`、`ImageBatch`、`AudioEncoderEncode`、`ImageFromBatch`、`WanInfiniteTalkToVideo`、`LoadAudio`、`UNETLoader`、`CreateVideo`、`CLIPTextEncode`、`SimpleCalculatorKJ`、`Audio Duration (mtb)`、`AudioConcat`、`LoadImage`、`SegmentV2`、`easy forLoopEnd`、`VHS_VideoCombine`、`SaveVideo`、`ZML_MaskSeparateDistance`、`JWInteger`、`PreviewAudio`、`ShowAnything|Mie`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
