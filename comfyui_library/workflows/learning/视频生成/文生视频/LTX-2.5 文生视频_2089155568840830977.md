---
key: 视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json
name: LTX-2.5 文生视频_2089155568840830977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json
hash: 619ece353d64ad53
coverage: 0.82
learned_at: 2026-10-15 22:44:43
nodes: [CreateVideo, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, CLIPLoader, ImageFromBatch, SaveAudio, MarkdownNote, MarkdownNote, PreviewAny, CLIPTextEncode, ComfySwitchNode, TextGenerateLTX2Prompt, PrimitiveStringMultiline, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVConcatAVLatent, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, SaveImage, ResolutionSelector, VHS_VideoCombine, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CreateVideo`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `ImageFromBatch`
- `SaveAudio`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `SaveImage`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`CreateVideo`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVDualCFGGuider`、`LTXVConditioning`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`ImageFromBatch`、`SaveAudio`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`SaveImage`、`ResolutionSelector`、`VHS_VideoCombine`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
