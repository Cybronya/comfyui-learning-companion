---
key: 视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json
name: LTX2.3数字人音频驱动视频生成_2031965741934714882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json
hash: be99da2caa3b7038
coverage: 0.827586
learned_at: 2026-10-15 22:45:09
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MelBandRoFormerSampler, SetNode, SolidMask, LTXVAudioVAELoader, GetNode, LTXVSeparateAVLatent, TrimAudioDuration, SetLatentNoiseMask, LTXVAudioVAEEncode, CheckpointLoaderSimple, PrimitiveInt, PrimitiveInt, PrimitiveNode, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, PrimitiveFloat, SaveVideo, CreateVideo, MelBandRoFormerModelLoader, ComfyMathExpression, LoadImage, LoadAudio, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXAVTextEncoderLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `SolidMask`
- `LTXVAudioVAELoader`
- `GetNode`
- `LTXVSeparateAVLatent`
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `SaveVideo`
- `CreateVideo`
- `MelBandRoFormerModelLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoadAudio`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXAVTextEncoderLoader`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（48/58）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`MelBandRoFormerSampler`、`SolidMask`、`LTXVAudioVAELoader`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`SaveVideo`、`CreateVideo`、`MelBandRoFormerModelLoader`、`LoadImage`、`LoadAudio`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
