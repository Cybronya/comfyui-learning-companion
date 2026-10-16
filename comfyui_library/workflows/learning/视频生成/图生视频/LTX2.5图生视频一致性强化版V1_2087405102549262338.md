---
key: 视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json
name: LTX2.5图生视频一致性强化版V1_2087405102549262338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json
hash: af3eb65f04b9374f
coverage: 0.830508
learned_at: 2026-10-16 21:27:37
nodes: [MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, PrimitiveInt, ResizeImageMaskNode, LTXVPreprocess, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, MarkdownNote, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, CLIPLoader, SaveVideo, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, LoadImage, ResolutionSelector, VAEDecodeTiled, CreateVideo, LTXVAudioVAEDecode, easy showAnything, CR Text, RH_LLMAPI_Pro_Node, TextGenerateLTX2Prompt, CR Text, LTXVImgToVideoInplace, PrimitiveBoolean, LoadImage, PreviewAny, VHS_VideoCombine, LTXVImgToVideoInplace, LTXVDualCFGGuider, UNETLoader, LTXVDualCFGGuider, ManualSigmas, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `MarkdownNote`
- `MarkdownNote`
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
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `SaveVideo`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `LoadImage`
- `ResolutionSelector`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `easy showAnything`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `TextGenerateLTX2Prompt`
- `CR Text`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `LoadImage`
- `PreviewAny`
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `LTXVDualCFGGuider`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`PrimitiveBoolean`、`CLIPLoader`、`SaveVideo`、`VAELoader`、`LatentUpscaleModelLoader`、`LoadImage`、`ResolutionSelector`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`CR Text`、`RH_LLMAPI_Pro_Node`、`TextGenerateLTX2Prompt`、`LTXVImgToVideoInplace`、`VHS_VideoCombine`、`LTXVDualCFGGuider`、`UNETLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
