---
key: 视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json
name: LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json
hash: 071caa63e5ef3dcb
coverage: 0.833333
learned_at: 2026-10-16 21:27:36
nodes: [SamplerEulerAncestral, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, ComfyMathExpression, MarkdownNote, RH_LLMAPI_Pro_Node, CLIPTextEncode, UNETLoader, VAELoader, VAELoader, CLIPLoader, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConditioning, LTXVAddGuide, LTXVAddGuide, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, VHS_VideoCombine, Label (rgthree), RandomNoise, PreviewAny, LTXVDualCFGGuider, Label (rgthree), LoadImage, SamplerCustomAdvanced, GetImageSize, LTXVPreprocess, CR Text, PrimitiveInt, PrimitiveStringMultiline, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `SamplerEulerAncestral` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVAddGuide`
- `LTXVAddGuide`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `RandomNoise`
- `PreviewAny`
- `LTXVDualCFGGuider`
- `Label (rgthree)`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `LTXVPreprocess`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`SamplerEulerAncestral`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVAddGuide`、`LoadImage`、`ResizeImageMaskNode`、`LTXVPreprocess`、`VHS_VideoCombine`、`Label (rgthree)`、`RandomNoise`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`GetImageSize`、`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
