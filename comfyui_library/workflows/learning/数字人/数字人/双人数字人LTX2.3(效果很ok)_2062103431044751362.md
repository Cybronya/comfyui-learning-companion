---
key: 数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json
name: 双人数字人LTX2.3(效果很ok)_2062103431044751362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json
hash: 16f233f0ed5242fc
coverage: 0.842105
learned_at: 2026-10-26 02:00:57
nodes: [LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, GetNode, LTXVLatentUpsampler, CheckpointLoaderSimple, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, EmptyLTXVLatentVideo, GetNode, MathExpression|pysssss, LTXVAudioVAEEncode, GetNode, LTXVImgToVideoConditionOnly, LatentUpscaleModelLoader, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, VAEDecodeTiled, LTXVConcatAVLatent, LTXVConditioning, CLIPTextEncode, Anything Everywhere, LTXVChunkFeedForward, ModelPatchTorchSettings, easy cleanGpuUsed, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTX2_NAG, KSampler, GetNode, VHS_VideoCombine, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, MathExpression|pysssss, KSampler, Anything Everywhere, LoraLoaderModelOnly, LoraLoaderModelOnly, SetLatentNoiseMask, SolidMask, Audio Duration (mtb), NormalizeAudioLoudness, GetNode, MathExpression|pysssss, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, AudioConcat, Text Multiline, LoadImage, LoadAudio, LoadAudio, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 0.4000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "simple", "seed": 695848243311130, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `LatentUpscaleModelLoader`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `Anything Everywhere`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `KSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MathExpression|pysssss`
- `KSampler` ★核心
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `Audio Duration (mtb)`
- `NormalizeAudioLoudness`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `AudioConcat`
- `Text Multiline`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `695848243311130`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **84%**（48/57）

**有卡**：`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM V2`、`LTXVLatentUpsampler`、`CheckpointLoaderSimple`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`LTXVAudioVAEEncode`、`LTXVImgToVideoConditionOnly`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`easy cleanGpuUsed`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEDecode`、`LTX2_NAG`、`KSampler`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`SetLatentNoiseMask`、`SolidMask`、`Audio Duration (mtb)`、`NormalizeAudioLoudness`、`AudioConcat`、`Text Multiline`、`LoadImage`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
