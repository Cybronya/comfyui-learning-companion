---
key: 视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json
name: Ltx2.5首尾帧生视频-极速版_2090424622050275330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json
hash: f97fee154633ee11
coverage: 0.825
learned_at: 2026-10-16 22:02:01
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, RandomNoise, SamplerEulerAncestral, ManualSigmas, CLIPTextEncode, PrimitiveInt, ResizeImageMaskNode, ResizeImageMaskNode, ComfyMathExpression, EmptyLTXVLatentVideo, GetImageSize, LTXVConditioning, CLIPTextEncode, LTXVAddGuide, LTXVAddGuide, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, LTXVCropGuides, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, TextGenerateLTX2Prompt, PreviewAny, LTXVConcatAVLatent, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, ResolutionSelector, SaveVideo, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `RandomNoise`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVAddGuide`
- `LTXVAddGuide`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `ResolutionSelector`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`ComfyMathExpression`、`RandomNoise`、`SamplerEulerAncestral`、`ManualSigmas`、`CLIPTextEncode`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`GetImageSize`、`LTXVConditioning`、`LTXVAddGuide`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`TextGenerateLTX2Prompt`、`LTXVConcatAVLatent`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`SaveVideo`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral
