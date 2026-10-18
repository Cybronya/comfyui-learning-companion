---
key: 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json
name: LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json
hash: 8a142fcb45bf679f
coverage: 0.753425
learned_at: 2026-10-15 22:35:29
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CheckpointLoaderSimple, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CFGGuider, LTXVAudioVAELoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVEmptyLatentAudio, MarkdownNote, easy showAnything, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImageMaskNode, LTXAVTextEncoderLoader, CLIPTextEncode, Note, CLIPTextEncode, TrimAudioDuration, MelBandRoFormerModelLoader, SoundFlow_GetLength, CM_FloatToInt, MelBandRoFormerSampler, SolidMask, SimpleMath+, easy showAnything, LTXVAudioVAEEncode, SetLatentNoiseMask, Note, PrimitiveStringMultiline, Note, Note, Note, LoadAudio, LoadImage, PrimitiveStringMultiline, LayerUtility: ImageScaleByAspectRatio V2, Note, Int, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, MarkdownNote, VAEDecodeTiled, CreateVideo, SaveVideo, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031213206097633281.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `easy showAnything`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `TrimAudioDuration`
- `MelBandRoFormerModelLoader`
- `SoundFlow_GetLength`
- `CM_FloatToInt`
- `MelBandRoFormerSampler` ★核心
- `SolidMask`
- `SimpleMath+`
- `easy showAnything`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `Note`
- `PrimitiveStringMultiline`
- `Note`
- `Note`
- `Note`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Int`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `SaveVideo`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（55/73）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`SoundFlow_GetLength`、`CM_FloatToInt`、`MelBandRoFormerSampler`、`SolidMask`、`SimpleMath+`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoadAudio`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`PrimitiveBoolean`、`VAEDecodeTiled`、`CreateVideo`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
