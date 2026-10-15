---
key: 视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json
name: 图生视频LTX2.3_kijai_fp8_2043785559667122178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json
hash: 8d4626e499c1d14c
coverage: 0.816667
learned_at: 2026-10-15 22:48:24
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, Reroute, EmptyLTXVLatentVideo, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, ResizeImageMaskNode, KSamplerSelect, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CLIPTextEncode, VAELoaderKJ, DualCLIPLoader, UNETLoader, ComfyMathExpression, SimpleMath+, PrimitiveInt, PrimitiveBoolean, ResizeImagesByLongerEdge, LTXVPreprocess, CLIPTextEncode, LTXVConditioning, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, PrimitiveInt, LTXVLatentUpsampler, LatentUpscaleModelLoader, CFGGuider, PrimitiveInt, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, LoadImage, SaveVideo, INTConstant, PrimitiveInt, LTXVImgToVideoInplace, ComfyMathExpression, INTConstant, ComfyMathExpression, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PreviewAudio, LoadAudio, LTXVAudioVAEEncode, SetNode, NormalizeAudioLoudness, TrimAudioDuration, AudioConcat, GetNode, SetNode, VAELoaderKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频LTX2.3_kijai_fp8_2043785559667122178.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `SimpleMath+`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`
- `INTConstant`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `INTConstant`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `PreviewAudio`
- `LoadAudio`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `NormalizeAudioLoudness`
- `TrimAudioDuration`
- `AudioConcat`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（49/60）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`ComfyMathExpression`、`SimpleMath+`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVConditioning`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LoadImage`、`SaveVideo`、`INTConstant`、`LTXVEmptyLatentAudio`、`PreviewAudio`、`LoadAudio`、`LTXVAudioVAEEncode`、`NormalizeAudioLoudness`、`TrimAudioDuration`、`AudioConcat`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
