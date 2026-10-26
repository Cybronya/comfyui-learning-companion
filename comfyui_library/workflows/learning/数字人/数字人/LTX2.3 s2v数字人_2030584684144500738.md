---
key: 数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json
name: LTX2.3 s2v数字人_2030584684144500738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json
hash: 3abcce367517760e
coverage: 0.881356
learned_at: 2026-10-26 01:55:50
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, LTXVPreprocess, LTXVImgToVideoInplace, CheckpointLoaderSimple, CFGGuider, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, ManualSigmas, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, PreviewAudio, TrimAudioDuration, FloatConstant, PreviewAny, SimpleMath+, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Fast Groups Bypasser (rgthree), SaveVideo, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, PrimitiveStringMultiline, ImageLoader, ResizeImagesByLongerEdge, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
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
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `PreviewAudio`
- `TrimAudioDuration`
- `FloatConstant`
- `PreviewAny`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ImageLoader`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（52/59）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`ComfyMathExpression`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`PreviewAudio`、`TrimAudioDuration`、`FloatConstant`、`SimpleMath+`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`SaveVideo`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ImageLoader`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
