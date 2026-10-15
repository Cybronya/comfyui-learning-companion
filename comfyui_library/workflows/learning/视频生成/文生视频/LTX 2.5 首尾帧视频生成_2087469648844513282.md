---
key: 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json
name: LTX 2.5 首尾帧视频生成_2087469648844513282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json
hash: b0a7f8b2e5e1f52b
coverage: 0.829268
learned_at: 2026-10-15 22:44:35
nodes: [LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, RandomNoise, CLIPTextEncode, GetImageSize, LTXVDualCFGGuider, PrimitiveInt, PrimitiveInt, PrimitiveInt, TextGenerateLTX2Prompt, PrimitiveBoolean, UNETLoader, VAELoader, VAELoader, CLIPTextEncode, LTXVPreprocess, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, VHS_VideoCombine, ComfyMathExpression, ComfyMathExpression, VAEDecodeTiled, ComfySwitchNode, PreviewAny, PrimitiveStringMultiline, LoadImage, LoadImage, CLIPLoader, CLIPLoader, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（41 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
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
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LTXVDualCFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `ComfySwitchNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVDualCFGGuider`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`LTXVPreprocess`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`ComfyMathExpression`、`VAEDecodeTiled`、`LoadImage`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
