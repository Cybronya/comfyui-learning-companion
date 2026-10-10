---
key: 视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json
name: video_ltx2_custom_voice_kijai_multi_2031409117054640130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json
hash: eb66cdd9a1ab4ea8
coverage: 0.859649
learned_at: 2026-10-11 03:16:51
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ComfyMathExpression, Reroute, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveBoolean, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, VAEDecodeTiled, MarkdownNote, MarkdownNote, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, KSamplerSelect, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVConditioning, CLIPTextEncode, CFGGuider, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVImgToVideoInplace, CLIPTextEncode, VAELoaderKJ, DualCLIPLoader, MelBandRoFormerSampler, LTXVAudioVAEEncode, MelBandRoFormerModelLoader, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, SetLatentNoiseMask, VAELoaderKJ, UNETLoader, LoadImage, PrimitiveInt, PrimitiveInt, SaveVideo, CreateVideo, AudioConcat, PrimitiveStringMultiline, LoadAudio, LoadAudio, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `CreateVideo`
- `AudioConcat`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveInt`

## 知识

覆盖率 **86%**（49/57）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`DualCLIPLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`MelBandRoFormerModelLoader`、`SimpleCalculatorKJ`、`SolidMask`、`TrimAudioDuration`、`SetLatentNoiseMask`、`UNETLoader`、`LoadImage`、`SaveVideo`、`CreateVideo`、`AudioConcat`、`LoadAudio`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
