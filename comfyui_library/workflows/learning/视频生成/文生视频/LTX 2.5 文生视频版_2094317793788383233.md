---
key: 视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json
name: LTX 2.5 文生视频版_2094317793788383233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json
hash: f74f72ea08748b1c
coverage: 0.770833
learned_at: 2026-10-15 22:44:35
nodes: [LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfySwitchNode, PreviewAny, CLIPTextEncode, CLIPTextEncode, LTXVDualCFGGuider, RandomNoise, LTXVConditioning, KSamplerSelect, PrimitiveBoolean, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SaveVideo, SamplerCustomAdvanced, CreateVideo, LTXVSeparateAVLatent, VAEDecodeTiled, ResolutionSelector, PrimitiveStringMultiline, CLIPLoader, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
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
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVDualCFGGuider`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`SaveVideo`、`CreateVideo`、`VAEDecodeTiled`、`ResolutionSelector`、`TextGenerateLTX2Prompt`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
