---
key: 视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json
name: video_ltx2_custom_voice_kijai_single_2031404838935859202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json
hash: 3755ac10ee6818a8
coverage: 0.854545
learned_at: 2026-10-11 03:16:51
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ComfyMathExpression, Reroute, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveBoolean, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, VAEDecodeTiled, MarkdownNote, MarkdownNote, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, KSamplerSelect, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVConditioning, CLIPTextEncode, CFGGuider, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVImgToVideoInplace, CLIPTextEncode, VAELoaderKJ, DualCLIPLoader, MelBandRoFormerSampler, LTXVAudioVAEEncode, MelBandRoFormerModelLoader, PrimitiveInt, PrimitiveInt, SimpleCalculatorKJ, PrimitiveInt, SolidMask, TrimAudioDuration, CreateVideo, PrimitiveStringMultiline, SetLatentNoiseMask, VAELoaderKJ, LoadAudio, UNETLoader, LoadImage, PrimitiveInt, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json`

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
- `ComfyMathExpression`
- `Reroute`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `PrimitiveBoolean`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerModelLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleCalculatorKJ`
- `PrimitiveInt`
- `SolidMask`
- `TrimAudioDuration`
- `CreateVideo`
- `PrimitiveStringMultiline`
- `SetLatentNoiseMask`
- `VAELoaderKJ`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveInt`
- `SaveVideo`

## 知识

覆盖率 **85%**（47/55）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`DualCLIPLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`MelBandRoFormerModelLoader`、`SimpleCalculatorKJ`、`SolidMask`、`TrimAudioDuration`、`CreateVideo`、`SetLatentNoiseMask`、`LoadAudio`、`UNETLoader`、`LoadImage`、`SaveVideo`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
