---
key: 视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json
name: LTX 2.5 首尾帧生视频版_2094313555356119041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json
hash: 011fcdcd53a0014f
coverage: 0.777778
learned_at: 2026-10-16 23:42:02
nodes: [LTXVAddGuide, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVConditioning, CreateVideo, GetImageSize, LTXVPreprocess, ResizeImageMaskNode, ResizeImageMaskNode, VAELoader, VAELoader, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, MarkdownNote, CLIPTextEncode, CLIPLoader, UNETLoader, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVDualCFGGuider, SamplerEulerAncestral, ManualSigmas, RandomNoise, LTXVCropGuides, PrimitiveBoolean, ComfySwitchNode, LTXVAddGuide, PrimitiveInt, SaveVideo, MarkdownNote, MarkdownNote, CLIPLoader, TextGenerateLTX2Prompt, LoadImage, LoadImage, CLIPTextEncode, PreviewAny, LTXVPreprocess, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `CreateVideo`
- `GetImageSize`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVCropGuides`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `LTXVAddGuide`
- `PrimitiveInt`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`LTXVAddGuide`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CreateVideo`、`GetImageSize`、`LTXVPreprocess`、`ResizeImageMaskNode`、`VAELoader`、`ComfyMathExpression`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`SamplerEulerAncestral`、`ManualSigmas`、`RandomNoise`、`LTXVCropGuides`、`PrimitiveBoolean`、`SaveVideo`、`TextGenerateLTX2Prompt`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
