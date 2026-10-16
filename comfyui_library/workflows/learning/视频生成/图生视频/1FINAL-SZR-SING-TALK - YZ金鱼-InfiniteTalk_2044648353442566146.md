---
key: 视频生成/图生视频/1FINAL-SZR-SING-TALK - YZ金鱼-InfiniteTalk_2044648353442566146.json
name: 1FINAL-SZR-SING-TALK - YZ金鱼-InfiniteTalk_2044648353442566146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044648353442566146.json
hash: a348ad3b74ea7200
coverage: 0.361905
learned_at: 2026-10-15 22:36:39
nodes: [CLIPTextEncode, VAELoader, SetNode, SetNode, GetNode, CLIPVisionEncode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Any2ListNode, SetNode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, VHS_VideoCombine, KSampler, CLIPTextEncode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, WanInfiniteTalkToVideo, GetNode, GetNode, VHS_VideoCombine, CLIPTextEncode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, WanInfiniteTalkToVideo, GetNode, GetNode, SetNode, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, GetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, Note, AudioSeparation, easy promptLine, WanInfiniteTalkToVideo, AudioCrop, Audio Duration (mtb), MathExpression|pysssss, MathExpression|pysssss, VAEDecode, VAEDecode, VAEDecode, GetNode, SetNode, SetNode, ImageFromBatch, WanInfiniteTalkToVideo, GetNode, ImageFromBatch, ImageBatch, KSampler, ImageBatch, CLIPTextEncode, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, Reroute, GetNode, GetNode, VHS_VideoCombine, WanInfiniteTalkToVideo, VAEDecode, ImageBatch, ImageFromBatch, Reroute, GetNode, GetNode, Reroute, VHS_VideoCombine, SetNode, CLIPLoader, SetNode, easy showAnything, ImageBatch, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, ImageFromBatch, VAEDecode, ImageBatch, Reroute, LayerUtility: ImageScaleByAspectRatio V2, easy int, SetNode, easy int, PrimitiveFloat, easy int, DiffusionModelLoaderKJ, SetNode, AudioEncoderEncode, ModelPatchLoader, AudioEncoderLoader, GetNode, GetNode, GetNode, GetNode, GetNode, WanInfiniteTalkToVideo, PreviewAudio, CLIPTextEncode, easy indexAnything, CLIPTextEncode, easy indexAnything, CLIPTextEncode, easy indexAnything, CLIPTextEncode, easy indexAnything, CLIPTextEncode, easy indexAnything, CLIPTextEncode, easy indexAnything, LoadImage, VHS_VideoCombine, PreviewAudio, TextInput_, MarkdownNote, LoadAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 76562718299725, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/1FINAL-SZR-SING-TALK - YZ金鱼-InfiniteTalk_2044648353442566146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044648353442566146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（210 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Any2ListNode`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `WanInfiniteTalkToVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `Note`
- `AudioSeparation`
- `easy promptLine`
- `WanInfiniteTalkToVideo`
- `AudioCrop`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `WanInfiniteTalkToVideo`
- `GetNode`
- `ImageFromBatch`
- `ImageBatch`
- `KSampler` ★核心
- `ImageBatch`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `Reroute`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `VAEDecode` ★核心
- `ImageBatch`
- `ImageFromBatch`
- `Reroute`
- `GetNode`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `easy showAnything`
- `ImageBatch`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `ImageBatch`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `SetNode`
- `easy int`
- `PrimitiveFloat`
- `easy int`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `AudioEncoderEncode`
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanInfiniteTalkToVideo`
- `PreviewAudio`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `LoadImage`
- `VHS_VideoCombine`
- `PreviewAudio`
- `TextInput_`
- `MarkdownNote`
- `LoadAudio`

## 关键参数

- `seed` = `76562718299725`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **36%**（76/210）

**有卡**：`CLIPTextEncode`、`VAELoader`、`CLIPVisionEncode`、`Any2ListNode`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`WanInfiniteTalkToVideo`、`CLIPVisionLoader`、`AudioSeparation`、`easy promptLine`、`AudioCrop`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`ImageFromBatch`、`ImageBatch`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`DiffusionModelLoaderKJ`、`AudioEncoderEncode`、`ModelPatchLoader`、`AudioEncoderLoader`、`PreviewAudio`、`easy indexAnything`、`LoadImage`、`TextInput_`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、AudioEncoderLoader、CLIPVisionEncode

## 参数体检

发现 6 个问题：
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
