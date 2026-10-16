---
key: 视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json
name: 【开源】LTX2.5 首尾帧生视频_2087467308766814210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json
hash: 2d71d68f7318da83
coverage: 0.8125
learned_at: 2026-10-16 21:27:59
nodes: [VAEDecodeTiled, PrimitiveBoolean, CLIPLoader, LTXVConcatAVLatent, UNETLoader, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, VAELoader, VAELoader, SamplerEulerAncestral, ManualSigmas, RandomNoise, LTXVDualCFGGuider, LTXVCropGuides, LTXVAddGuide, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, GetImageSize, LTXVPreprocess, CLIPLoader, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAddGuide, LTXVPreprocess, ResizeImageMaskNode, LoadImage, LoadImage, TextGenerateLTX2Prompt, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, ResolutionSelector, LTXVEmptyLatentAudio, SamplerCustomAdvanced, easy cleanGpuUsed, easy showAnything, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `VAEDecodeTiled` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `LTXVCropGuides`
- `LTXVAddGuide`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `GetImageSize`
- `LTXVPreprocess`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVAddGuide`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `ResolutionSelector`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `ComfySwitchNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`VAEDecodeTiled`、`PrimitiveBoolean`、`CLIPLoader`、`LTXVConcatAVLatent`、`UNETLoader`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`VAELoader`、`SamplerEulerAncestral`、`ManualSigmas`、`RandomNoise`、`LTXVDualCFGGuider`、`LTXVCropGuides`、`LTXVAddGuide`、`ResizeImageMaskNode`、`GetImageSize`、`LTXVPreprocess`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`、`TextGenerateLTX2Prompt`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`ResolutionSelector`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral
