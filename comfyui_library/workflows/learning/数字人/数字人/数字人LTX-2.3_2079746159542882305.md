---
key: 数字人/数字人/数字人LTX-2.3_2079746159542882305.json
name: 数字人LTX-2.3_2079746159542882305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人LTX-2.3_2079746159542882305.json
hash: 3fc1bceef8e3b115
coverage: 0.863636
learned_at: 2026-10-26 02:02:37
nodes: [LoadImage, LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, CheckpointLoaderSimple, VAELoaderKJ, SetNode, DualCLIPLoader, Anything Everywhere, SetNode, CLIPTextEncode, LoraLoaderModelOnly, MathExpression|pysssss, LTXVImgToVideoConditionOnly, GetNode, LTXVConcatAVLatent, MathExpression|pysssss, GetNode, Audio Resample (mtb), AudioCombine, GetNode, LTXVImgToVideoConditionOnly, LatentUpscaleModelLoader, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, VAEDecodeTiled, LTXVConcatAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, Anything Everywhere, LTXVChunkFeedForward, ModelPatchTorchSettings, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, AudioCombine, AudioSeparation, AudioCombine, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, Float, Audio Duration (mtb), MathExpression|pysssss, LayerUtility: If , MathExpression|pysssss, CLIPTextEncode, Text Multiline, LayerUtility: If , LayerUtility: BooleanOperatorV2, LoadAudio, LoraLoaderModelOnly, NormalizeAudioLoudness, NormalizeAudioLoudness, SolidMask, SetLatentNoiseMask, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, KSampler, LTXVConditioning, GetNode, VHS_VideoCombine, LTXVSeparateAVLatent, TrimAudioDuration]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 1, "sampler_name": "heun", "scheduler": "linear_quadratic", "seed": 547311220077528, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/数字人LTX-2.3_2079746159542882305.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人LTX-2.3_2079746159542882305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（66 个）：
- `LoadImage`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `Anything Everywhere`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `MathExpression|pysssss`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `LTXVConcatAVLatent`
- `MathExpression|pysssss`
- `GetNode`
- `Audio Resample (mtb)`
- `AudioCombine`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `LatentUpscaleModelLoader`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `Anything Everywhere`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode` ★核心
- `AudioCombine`
- `AudioSeparation`
- `AudioCombine`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `Float`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `LayerUtility: If `
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `SolidMask`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `LTXVConditioning`
- `GetNode`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `TrimAudioDuration`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `547311220077528`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **86%**（57/66）

**有卡**：`LoadImage`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CheckpointLoaderSimple`、`VAELoaderKJ`、`DualCLIPLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`MathExpression|pysssss`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`Audio Resample (mtb)`、`AudioCombine`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVAudioVAEDecode`、`AudioSeparation`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`Float`、`Audio Duration (mtb)`、`LayerUtility: If `、`Text Multiline`、`LayerUtility: BooleanOperatorV2`、`LoadAudio`、`NormalizeAudioLoudness`、`SolidMask`、`SetLatentNoiseMask`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`LTXVConditioning`、`VHS_VideoCombine`、`TrimAudioDuration`

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
