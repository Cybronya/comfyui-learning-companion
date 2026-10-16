---
key: 视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json
name: LTX2.5首尾帧生视频2608_2095393045469556738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json
hash: 251f66692c939f3b
coverage: 0.782609
learned_at: 2026-10-17 00:02:15
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, ComfySwitchNode, GetImageSize, LTXVPreprocess, LTXVPreprocess, TextGenerateLTX2Prompt, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveStringMultiline, LTXVAudioVAEDecode, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, VHS_VideoCombine, VAEDecodeTiled, LoadImage, LoadImage, CLIPLoader, PrimitiveBoolean, PrimitiveInt, VHS_VideoCombine, FlashVSRNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `FlashVSRNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LoadImage`、`PrimitiveBoolean`、`FlashVSRNode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
