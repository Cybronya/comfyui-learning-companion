---
key: 视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json
name: LTX2.5文生视频_2087526329527922689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json
hash: 42685eac6a1efabb
coverage: 0.8
learned_at: 2026-10-11 20:53:38
nodes: [ComfySwitchNode, LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, RandomNoise, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, MarkdownNote, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, PreviewAny, ResolutionSelector, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, LatentUpscaleModelLoader, TextGenerateLTX2Prompt, SamplerCustomAdvanced, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, VHS_VideoCombine, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json`

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
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `TextGenerateLTX2Prompt`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `孤海注释`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
