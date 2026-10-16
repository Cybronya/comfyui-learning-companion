---
key: 视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json
name: LTX2.5图生视频（标准版工作流）_2087460376823820290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json
hash: 0ffdff2db858da21
coverage: 0.823529
learned_at: 2026-10-16 21:27:37
nodes: [KSamplerSelect, ComfyMathExpression, ComfyMathExpression, MarkdownNote, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, MarkdownNote, PrimitiveInt, ResolutionSelector, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, CR Text, LoadImage, MarkdownNote, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, CR Text, RH_LLMAPI_Pro_Node, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（51 个）：
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `PrimitiveInt`
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CR Text`
- `LoadImage`
- `MarkdownNote`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（42/51）

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ResolutionSelector`、`CLIPTextEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CR Text`、`LoadImage`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
