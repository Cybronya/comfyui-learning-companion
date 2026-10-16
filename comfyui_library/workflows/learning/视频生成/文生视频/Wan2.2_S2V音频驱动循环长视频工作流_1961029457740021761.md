---
key: 视频生成/文生视频/Wan2.2_S2V音频驱动循环长视频工作流_1961029457740021761.json
name: Wan2.2_S2V音频驱动循环长视频工作流_1961029457740021761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1961029457740021761.json
hash: eae17dd775bf1e6d
coverage: 0.577465
learned_at: 2026-10-15 22:43:43
nodes: [SetNode, SetNode, SetNode, easy showAnything, MathExpression|pysssss, GetNode, MathExpression|pysssss, VHS_GetImageCount, easy showAnything, easy showAnything, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, SetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_GetImageCount, GetNode, MathExpression|pysssss, SetNode, VHS_GetImageCount, MathExpression|pysssss, MathExpression|pysssss, Note, easy forLoopStart, easy forLoopEnd, GetNode, ImageBatchMulti, GetNode, GetNode, GetNode, LoadImage, MathExpression|pysssss, SetNode, SetNode, AudioSeparation, SetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, AudioSeparation, easy cleanGpuUsed, VAEDecode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AudioEncoderEncode, AudioEncoderLoader, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, AudioEncoderEncode, AudioEncoderLoader, GetNode, GetNode, GetImageRangeFromBatch, MathExpression|pysssss, MathExpression|pysssss, LayerUtility: PurgeVRAM, VAEDecode, AudioSeparation, MathExpression|pysssss, CLIPTextEncode, SetNode, ImageResizeKJv2, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, KSampler, SetNode, GetNode, Reroute, KSampler, GetNode, VHS_VideoCombine, SetNode, INTConstant, FloatConstant, LoadImage, LoadImage, WanSoundImageToVideo, WanSoundImageToVideo, INTConstant, SetNode, GetNode, GetNode, ImageResizeKJv2, CR Image Input Switch (4 way), LoadImage, ModelSamplingSD3, SetNode, CLIPLoader, VHS_LoadAudioUpload, LoadAudio, VAELoader, ImageFromBatch, PathchSageAttentionKJ, LoraLoaderModelOnly, VHS_VideoCombine, GetNode, UnetLoaderGGUF, LoraLoaderModelOnly, wanBlockSwap, TorchCompileModelWanVideoV2, LoadImage, UNETLoader, INTConstant, easy seed, VHS_VideoCombine, GetNode, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 400305022224497, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2_S2V音频驱动循环长视频工作流_1961029457740021761.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1961029457740021761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（142 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Note`
- `easy forLoopStart`
- `easy forLoopEnd`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `AudioSeparation`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioSeparation`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `AudioSeparation`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SetNode`
- `GetNode`
- `Reroute`
- `KSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `INTConstant`
- `FloatConstant`
- `LoadImage`
- `LoadImage`
- `WanSoundImageToVideo`
- `WanSoundImageToVideo`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `CR Image Input Switch (4 way)`
- `LoadImage`
- `ModelSamplingSD3`
- `SetNode`
- `CLIPLoader`
- `VHS_LoadAudioUpload`
- `LoadAudio`
- `VAELoader`
- `ImageFromBatch`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `TorchCompileModelWanVideoV2`
- `LoadImage`
- `UNETLoader` ★核心
- `INTConstant`
- `easy seed`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `400305022224497`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（82/142）

**有卡**：`MathExpression|pysssss`、`VHS_GetImageCount`、`LayerUtility: PurgeVRAM`、`easy forLoopStart`、`easy forLoopEnd`、`ImageBatchMulti`、`LoadImage`、`AudioSeparation`、`easy cleanGpuUsed`、`VAEDecode`、`AudioEncoderEncode`、`AudioEncoderLoader`、`GetImageRangeFromBatch`、`CLIPTextEncode`、`ImageResizeKJv2`、`KSampler`、`VHS_VideoCombine`、`INTConstant`、`FloatConstant`、`WanSoundImageToVideo`、`CR Image Input Switch (4 way)`、`ModelSamplingSD3`、`CLIPLoader`、`VHS_LoadAudioUpload`、`LoadAudio`、`VAELoader`、`ImageFromBatch`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`wanBlockSwap`、`TorchCompileModelWanVideoV2`、`UNETLoader`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
