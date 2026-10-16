---
key: 视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json
name: LTX2.5图生视频_2087526346007339010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json
hash: 55d1c2f953ea3254
coverage: 0.777778
learned_at: 2026-10-16 21:27:36
nodes: [MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ComfySwitchNode, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, TextGenerateLTX2Prompt, ComfyMathExpression, MarkdownNote, PreviewAny, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, CLIPLoader, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, LoadImage, PrimitiveInt, LTXVAudioVAEDecode, VAEDecodeTiled, ComfyMathExpression, PrimitiveStringMultiline, 孤海注释, ResolutionSelector, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（54 个）：
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `MarkdownNote`
- `PreviewAny`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `LoadImage`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `孤海注释`
- `ResolutionSelector`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TextGenerateLTX2Prompt`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`LoadImage`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ResolutionSelector`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
