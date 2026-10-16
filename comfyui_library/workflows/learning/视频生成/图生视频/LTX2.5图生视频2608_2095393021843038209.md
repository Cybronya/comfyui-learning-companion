---
key: 视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json
name: LTX2.5图生视频2608_2095393021843038209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json
hash: beba8c6077846873
coverage: 0.8
learned_at: 2026-10-17 00:02:15
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, TextGenerateLTX2Prompt, CLIPTextEncode, ComfySwitchNode, PreviewAny, PrimitiveBoolean, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, UNETLoader, PrimitiveBoolean, CLIPLoader, CLIPLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, PrimitiveStringMultiline, ResolutionSelector, PrimitiveInt, LoadImage, FlashVSRNode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（55 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextGenerateLTX2Prompt`
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `PreviewAny`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveInt`
- `LoadImage`
- `FlashVSRNode`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`TextGenerateLTX2Prompt`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVConditioning`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`UNETLoader`、`CLIPLoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ResolutionSelector`、`LoadImage`、`FlashVSRNode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
