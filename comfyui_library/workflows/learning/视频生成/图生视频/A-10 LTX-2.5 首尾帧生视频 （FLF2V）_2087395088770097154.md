---
key: 视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json
name: A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json
hash: 784eee4f84b2c89f
coverage: 0.8125
learned_at: 2026-10-16 21:27:26
nodes: [SaveVideo, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, CreateVideo, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, ComfySwitchNode, GetImageSize, LTXVPreprocess, LTXVPreprocess, TextGenerateLTX2Prompt, ImageScale, ImageScale, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, PrimitiveStringMultiline, ImageFromBatch, SaveImage, SaveAudio, VHS_VideoCombine, MarkdownNote, MarkdownNote, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SaveVideo`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
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
- `CreateVideo`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ImageScale`
- `ImageScale`
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`SaveVideo`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`CreateVideo`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ImageScale`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`PrimitiveBoolean`、`ComfyMathExpression`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
