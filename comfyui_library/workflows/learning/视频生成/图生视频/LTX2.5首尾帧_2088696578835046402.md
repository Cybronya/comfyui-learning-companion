---
key: 视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json
name: LTX2.5首尾帧_2088696578835046402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json
hash: ba375efd08f68455
coverage: 0.777778
learned_at: 2026-10-16 21:43:22
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, LoadImage, CreateVideo, SaveVideo, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, PrimitiveBoolean, PrimitiveStringMultiline, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
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
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LoadImage`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `ComfySwitchNode`
- `PreviewAny`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`LoadImage`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`GetImageSize`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
