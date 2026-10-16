---
key: 视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json
name: LTX2.5图生视频一致性加强版V1_2087536517580414978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json
hash: 329eb7edb804ed47
coverage: 0.823529
learned_at: 2026-10-16 21:27:36
nodes: [PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, CLIPLoader, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVImgToVideoInplace, LTXVImgToVideoInplace, LTXVDualCFGGuider, UNETLoader, LTXVDualCFGGuider, ManualSigmas, CR Text, LoadImage, PrimitiveBoolean, MarkdownNote, MarkdownNote, RH_LLMAPI_Pro_Node, PreviewAny, MarkdownNote, VHS_VideoCombine, LatentUpscaleModelLoader, ResolutionSelector, PrimitiveInt, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（51 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
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
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `LTXVDualCFGGuider`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `CR Text`
- `LoadImage`
- `PrimitiveBoolean`
- `MarkdownNote`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `ResolutionSelector`
- `PrimitiveInt`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（42/51）

**有卡**：`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplace`、`LTXVDualCFGGuider`、`UNETLoader`、`CR Text`、`LoadImage`、`PrimitiveBoolean`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
