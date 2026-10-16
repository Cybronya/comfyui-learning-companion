---
key: 视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json
name: LTX2.5首尾帧_2087405087823060994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json
hash: 8ff0cb451c2a992f
coverage: 0.785714
learned_at: 2026-10-16 21:27:37
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, ResizeImageMaskNode, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, CLIPLoader, PreviewAny, RH_LLMAPI_Pro_Node, CR Text, LoadImage, LoadImage, PrimitiveStringMultiline, VHS_VideoCombine, LTXVCropGuides, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`ResizeImageMaskNode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`UNETLoader`、`VAELoader`、`GetImageSize`、`CLIPLoader`、`RH_LLMAPI_Pro_Node`、`CR Text`、`LoadImage`、`VHS_VideoCombine`、`LTXVCropGuides`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
