---
key: 视频生成/图生视频/Wan2.2_S2V-数字人-多图片-超长视频制作_1971055874456358913.json
name: Wan2.2_S2V-数字人-多图片-超长视频制作_1971055874456358913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971055874456358913.json
hash: 1dc5a4e92b3d7d06
coverage: 0.557377
learned_at: 2026-10-15 22:31:55
nodes: [LayerUtility: PurgeVRAM, CLIPTextEncode, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, FloatConstant, CLIPLoader, INTConstant, easy seed, INTConstant, SetNode, KSampler, Note, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, LoadImage, LoadImage, LoadImage, CR Image Input Switch, INTConstant, SetNode, SetNode, VAELoader, SetNode, LoadImage, AudioEncoderLoader, GetNode, AudioSeparation, AudioEncoderEncode, WanSoundImageToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, GetNode, SetNode, VHS_GetImageCount, VHS_VideoCombine, ImageBatchMulti, GetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, KSampler, easy cleanGpuUsed, VAEDecode, LayerUtility: PurgeVRAM, MathExpression|pysssss, GetNode, AudioSeparation, LoadAudio, ModelSamplingSD3, easy showAnything, PreviewImage, GetNode, GetNode, GetNode, AudioEncoderEncode, WanSoundImageToVideo, GetNode, GetNode, LayerUtility: PurgeVRAM, Reroute, VHS_VideoCombine, GetNode, GetNode, SetNode, GetNode, GetNode, Note, Note, SetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_LoadVideo, CR Image Input Switch (4 way), Int, LoadImage, Int, SetNode, Int, SetNode, SetNode, easy forLoopEnd, Int, ImageResizeKJv2, ImageResizeKJv2, easy forLoopStart, easy showAnything, MathExpression|pysssss, SetNode, Int, GetNode, AudioEncoderLoader, AudioSeparation, RHHiddenNodes, RHHiddenNodes, VHS_LoadAudioUpload]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 400305022224497, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2_S2V-数字人-多图片-超长视频制作_1971055874456358913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971055874456358913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `FloatConstant`
- `CLIPLoader`
- `INTConstant`
- `easy seed`
- `INTConstant`
- `SetNode`
- `KSampler` ★核心
- `Note`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Image Input Switch`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoadImage`
- `AudioEncoderLoader`
- `GetNode`
- `AudioSeparation`
- `AudioEncoderEncode`
- `WanSoundImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `GetNode`
- `AudioSeparation`
- `LoadAudio`
- `ModelSamplingSD3`
- `easy showAnything`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `WanSoundImageToVideo`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `CR Image Input Switch (4 way)`
- `Int`
- `LoadImage`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `easy forLoopEnd`
- `Int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy forLoopStart`
- `easy showAnything`
- `MathExpression|pysssss`
- `SetNode`
- `Int`
- `GetNode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_LoadAudioUpload`

## 关键参数

- `seed` = `400305022224497`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（68/122）

**有卡**：`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`easy cleanGpuUsed`、`FloatConstant`、`CLIPLoader`、`INTConstant`、`easy seed`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`LoadImage`、`CR Image Input Switch`、`VAELoader`、`AudioEncoderLoader`、`AudioSeparation`、`AudioEncoderEncode`、`WanSoundImageToVideo`、`VAEDecode`、`VHS_GetImageCount`、`VHS_VideoCombine`、`ImageBatchMulti`、`MathExpression|pysssss`、`LoadAudio`、`ModelSamplingSD3`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`CR Image Input Switch (4 way)`、`Int`、`easy forLoopEnd`、`ImageResizeKJv2`、`easy forLoopStart`、`RHHiddenNodes`、`VHS_LoadAudioUpload`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
