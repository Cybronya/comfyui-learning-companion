---
key: 视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json
name: LTX2.5-经典文生视频_2087564635775004674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json
hash: caa5af72d8a352ae
coverage: 0.770833
learned_at: 2026-10-15 22:45:16
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, TextGenerateLTX2Prompt, ComfySwitchNode, PreviewAny, LTXVConditioning, RandomNoise, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, RandomNoise, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, LTXVConcatAVLatent, ManualSigmas, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, ResolutionSelector, PrimitiveInt, PrimitiveInt, MarkdownNote, CLIPLoader, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, PrimitiveBoolean, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PreviewAny`
- `LTXVConditioning`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`ManualSigmas`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`ResolutionSelector`、`CLIPTextEncode`、`PrimitiveBoolean`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
