---
key: 视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json
name: LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json
hash: 142c1fa81a352a3c
coverage: 0.451613
learned_at: 2026-10-15 22:36:27
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVImgToVideoInplace, SolidMask, ResizeImagesByLongerEdge, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImageMaskNode, LTXVAudioVAEEncode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, PrimitiveBoolean, VAELoader, VAELoaderKJ, CLIPTextEncode, TextInput_, DualCLIPLoader, LatentUpscaleModelLoader, TrimAudioDuration, SimpleMath+, AudioInfo, Display Any (rgthree), AudioCrop, SimpleMath+, PrimitiveInt, SaveVideo, PrimitiveFloat, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ShowText|pysssss, RH_LLMAPI_NODE, UNETLoader, LTXVChunkFeedForward, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadAudio, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042456955284889601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LTXVAudioVAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `PrimitiveBoolean`
- `VAELoader`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `TrimAudioDuration`
- `SimpleMath+`
- `AudioInfo`
- `Display Any (rgthree)`
- `AudioCrop`
- `SimpleMath+`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `UNETLoader` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`

## 知识

覆盖率 **45%**（56/124）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`PrimitiveBoolean`、`VAELoader`、`VAELoaderKJ`、`TextInput_`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`TrimAudioDuration`、`SimpleMath+`、`AudioInfo`、`Display Any (rgthree)`、`AudioCrop`、`SaveVideo`、`ComfyMathExpression`、`RH_LLMAPI_NODE`、`UNETLoader`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
