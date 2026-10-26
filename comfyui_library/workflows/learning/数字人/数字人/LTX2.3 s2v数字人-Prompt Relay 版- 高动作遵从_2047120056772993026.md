---
key: 数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json
name: LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json
hash: a2729d48a675cd07
coverage: 0.890909
learned_at: 2026-10-26 01:55:49
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, LatentUpscaleModelLoader, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, CFGGuider, LTXVConditioning, ManualSigmas, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, PreviewAudio, TrimAudioDuration, PreviewAny, SimpleMath+, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Fast Groups Bypasser (rgthree), SaveVideo, ResizeImagesByLongerEdge, ResizeImageMaskNode, CLIPTextEncode, LTX2_NAG, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVConcatAVLatent, LTXVImgToVideoInplace, ImageLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadAudio, FloatConstant, LTXVImgToVideoInplace, PromptRelayEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `CFGGuider`
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `PreviewAudio`
- `TrimAudioDuration`
- `PreviewAny`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `ImageLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadAudio`
- `FloatConstant`
- `LTXVImgToVideoInplace`
- `PromptRelayEncode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`ComfyMathExpression`、`LTXVPreprocess`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`PreviewAudio`、`TrimAudioDuration`、`SimpleMath+`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`SaveVideo`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`CLIPTextEncode`、`LTX2_NAG`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoInplace`、`ImageLoader`、`LoadAudio`、`FloatConstant`、`PromptRelayEncode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
