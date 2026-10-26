---
key: 数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json
name: Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json
hash: 2fc11a447937902a
coverage: 0.883333
learned_at: 2026-10-26 01:56:27
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, SolidMask, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImageMaskNode, LatentUpscaleModelLoader, PrimitiveInt, PrimitiveInt, LTXVImgToVideoInplace, RandomNoise, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, ResizeImagesByLongerEdge, ComfyMathExpression, EmptyLTXVLatentVideo, PrimitiveBoolean, SaveVideo, CreateVideo, ComfyMathExpression, LoraLoaderModelOnly, LTXAVTextEncoderLoader, VAEDecodeTiled, LTXVSeparateAVLatent, easy cleanGpuUsed, KSamplerSelect, Fast Groups Bypasser (rgthree), PrimitiveFloat, CLIPTextEncode, PrimitiveStringMultiline, PrimitiveInt, TrimAudioDuration, SoundFlow_GetLength, Apply Whisper, MelBandRoFormerSampler, MelBandRoFormerModelLoader, LongCatVoiceCloneTTS, LoadImage, LoadAudio, Text]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SolidMask`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LatentUpscaleModelLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `SaveVideo`
- `CreateVideo`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `TrimAudioDuration`
- `SoundFlow_GetLength`
- `Apply Whisper`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `LongCatVoiceCloneTTS`
- `LoadImage`
- `LoadAudio`
- `Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（53/60）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`SaveVideo`、`CreateVideo`、`LTXAVTextEncoderLoader`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`TrimAudioDuration`、`SoundFlow_GetLength`、`Apply Whisper`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`LongCatVoiceCloneTTS`、`LoadImage`、`LoadAudio`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
