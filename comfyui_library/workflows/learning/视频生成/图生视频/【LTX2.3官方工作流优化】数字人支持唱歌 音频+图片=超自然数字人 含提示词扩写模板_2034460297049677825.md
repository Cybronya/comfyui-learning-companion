---
key: 视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json
name: 【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034460297049677825.json
hash: 702f067a51a403f4
coverage: 0.790323
learned_at: 2026-10-15 22:35:44
nodes: [RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, CLIPTextEncode, SamplerCustomAdvanced, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LTXAVTextEncoderLoader, CLIPTextEncode, LTXVConditioning, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, MarkdownNote, Note, Note, CheckpointLoaderSimple, PrimitiveBoolean, Note, RH_LLMAPI_Pro_Node, PlaySound|pysssss, SaveVideo, LTXVConcatAVLatent, LTXVAudioVAELoader, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, PrimitiveInt, TrimAudioDuration, Note, Note, Float, LoadImage, LoadAudio, PrimitiveInt, PrimitiveInt, Text, easy showAnything, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034460297049677825.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveBoolean`
- `Note`
- `RH_LLMAPI_Pro_Node`
- `PlaySound|pysssss`
- `SaveVideo`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `PrimitiveInt`
- `TrimAudioDuration`
- `Note`
- `Note`
- `Float`
- `LoadImage`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveInt`
- `Text`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **79%**（49/62）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`RH_LLMAPI_Pro_Node`、`PlaySound|pysssss`、`SaveVideo`、`LTXVAudioVAELoader`、`ComfyMathExpression`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`Float`、`LoadImage`、`LoadAudio`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
