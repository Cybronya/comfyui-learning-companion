---
key: 视频生成/图生视频/【AI小兵哥】Wan2.2_S2V-语音生成超长视频工作流_1995424593299091458.json
name: 【AI小兵哥】Wan2.2_S2V-语音生成超长视频工作流_1995424593299091458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1995424593299091458.json
hash: 778dc28cf8310295
coverage: 0.785714
learned_at: 2026-10-15 22:33:23
nodes: [CLIPLoader, AudioEncoderLoader, CLIPTextEncode, CLIPTextEncode, AudioSeparation, LatentConcat, LatentCut, VAEDecode, ModelSamplingSD3, WanSoundImageToVideo, VAELoader, AudioEncoderEncode, ImageFromBatch, KSampler, UNETLoader, easy cleanGpuUsed, easy forLoopEnd, VAEDecode, Reroute, AudioCrop, PrimitiveStringMultiline, INTConstant, PrimitiveFloat, easy int, SimpleMath+, easy mathInt, Reroute, SimpleMath+, easy int, easy showAnything, easy compare, easy compare, SimpleMathCondition+, easy mathInt, easy showAnything, SimpleMathCondition+, SimpleMathCondition+, easy showAnything, PreviewAny, PreviewAny, PreviewAny, easy forLoopStart, WanSoundImageToVideoExtend, KSampler, LatentConcat, KSampler, Reroute, WanSoundImageToVideoExtend, LatentConcat, LoadImage, LoadImage, VHS_LoadAudioUpload, PrimitiveFloat, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【AI小兵哥】Wan2.2_S2V-语音生成超长视频工作流_1995424593299091458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995424593299091458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
- `CLIPLoader`
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AudioSeparation`
- `LatentConcat`
- `LatentCut`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanSoundImageToVideo`
- `VAELoader`
- `AudioEncoderEncode`
- `ImageFromBatch`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `VAEDecode` ★核心
- `Reroute`
- `AudioCrop`
- `PrimitiveStringMultiline`
- `INTConstant`
- `PrimitiveFloat`
- `easy int`
- `SimpleMath+`
- `easy mathInt`
- `Reroute`
- `SimpleMath+`
- `easy int`
- `easy showAnything`
- `easy compare`
- `easy compare`
- `SimpleMathCondition+`
- `easy mathInt`
- `easy showAnything`
- `SimpleMathCondition+`
- `SimpleMathCondition+`
- `easy showAnything`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `easy forLoopStart`
- `WanSoundImageToVideoExtend`
- `KSampler` ★核心
- `LatentConcat`
- `KSampler` ★核心
- `Reroute`
- `WanSoundImageToVideoExtend`
- `LatentConcat`
- `LoadImage`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`CLIPLoader`、`AudioEncoderLoader`、`CLIPTextEncode`、`AudioSeparation`、`LatentConcat`、`LatentCut`、`VAEDecode`、`ModelSamplingSD3`、`WanSoundImageToVideo`、`VAELoader`、`AudioEncoderEncode`、`ImageFromBatch`、`KSampler`、`UNETLoader`、`easy cleanGpuUsed`、`easy forLoopEnd`、`AudioCrop`、`INTConstant`、`easy int`、`SimpleMath+`、`easy mathInt`、`easy compare`、`SimpleMathCondition+`、`easy forLoopStart`、`WanSoundImageToVideoExtend`、`LoadImage`、`VHS_LoadAudioUpload`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
