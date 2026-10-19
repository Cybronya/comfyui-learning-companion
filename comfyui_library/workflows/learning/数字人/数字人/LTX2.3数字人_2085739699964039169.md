---
key: 数字人/数字人/LTX2.3数字人_2085739699964039169.json
name: LTX2.3数字人_2085739699964039169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人_2085739699964039169.json
hash: 91582dd7975dc7db
coverage: 0.866667
learned_at: 2026-10-18 19:07:41
nodes: [LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, VAELoaderKJ, DualCLIPLoader, Anything Everywhere, CLIPTextEncode, MathExpression|pysssss, LTXVImgToVideoConditionOnly, GetNode, LTXVConcatAVLatent, MathExpression|pysssss, GetNode, GetNode, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVPreprocess, VAEDecodeTiled, LTXVConcatAVLatent, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, Audio Duration (mtb), MathExpression|pysssss, LayerUtility: If , MathExpression|pysssss, CLIPTextEncode, LayerUtility: BooleanOperatorV2, SolidMask, SetLatentNoiseMask, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, KSampler, LTXVConditioning, VHS_VideoCombine, LTXVSeparateAVLatent, TrimAudioDuration, LayerUtility: If , AudioSeparation, LatentUpscaleModelLoader, SetNode, CheckpointLoaderSimple, SetNode, LoraLoaderModelOnly, LTXVChunkFeedForward, Anything Everywhere, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ImageResizeKJv2, TTResolutionSelector, Text Multiline, Float, LoadAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 1, "sampler_name": "heun", "scheduler": "linear_quadratic", "seed": 546569423572963, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3数字人_2085739699964039169.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人_2085739699964039169.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（60 个）：
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `LTXVConcatAVLatent`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `LayerUtility: If `
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LayerUtility: BooleanOperatorV2`
- `SolidMask`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `TrimAudioDuration`
- `LayerUtility: If `
- `AudioSeparation`
- `LatentUpscaleModelLoader`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `Anything Everywhere`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `Text Multiline`
- `Float`
- `LoadAudio`

## 关键参数

- `seed` = `546569423572963`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（52/60）

**有卡**：`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`DualCLIPLoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`Audio Duration (mtb)`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`SolidMask`、`SetLatentNoiseMask`、`KSampler`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM V2`、`LTXVConditioning`、`VHS_VideoCombine`、`TrimAudioDuration`、`AudioSeparation`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImageResizeKJv2`、`TTResolutionSelector`、`Text Multiline`、`Float`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、LTXVLatentUpsampler、LTXVConcatAVLatent

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
