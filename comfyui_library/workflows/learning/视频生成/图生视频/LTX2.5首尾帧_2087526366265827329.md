---
key: 视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json
name: LTX2.5首尾帧_2087526366265827329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json
hash: 00751d5e2576fb39
coverage: 0.755556
learned_at: 2026-10-16 21:27:37
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, LTXVConcatAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, PrimitiveBoolean, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, 孤海注释, LoadImage, PrimitiveStringMultiline, LoadImage, PrimitiveInt, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `ComfySwitchNode`
- `PreviewAny`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `孤海注释`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`LTXVConcatAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`GetImageSize`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
