---
key: 视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json
name: 极速 文生视频 LTX2.5 音画同出_2087530875780157441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json
hash: 8f35bd1537ed86b5
coverage: 0.822222
learned_at: 2026-10-15 22:48:49
nodes: [ComfySwitchNode, LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, CLIPTextEncode, PrimitiveInt, VHS_VideoCombine, ResolutionSelector, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（45 个）：
- `ComfySwitchNode`
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `CLIPLoader`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ComfyMathExpression`、`VHS_VideoCombine`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
