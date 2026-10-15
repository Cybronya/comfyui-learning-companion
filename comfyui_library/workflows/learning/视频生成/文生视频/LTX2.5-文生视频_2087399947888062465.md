---
key: 视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json
name: LTX2.5-文生视频_2087399947888062465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json
hash: 5132306dcaf3afa8
coverage: 0.818182
learned_at: 2026-10-15 22:45:16
nodes: [LTXVDualCFGGuider, ComfyMathExpression, LTXVConcatAVLatent, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, VAELoader, SamplerCustomAdvanced, ResolutionSelector, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVLatentUpsampler, CLIPTextEncode, CLIPTextEncode, ManualSigmas, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVDualCFGGuider, RandomNoise, RandomNoise, KSamplerSelect, LTXVConditioning, PrimitiveStringMultiline, CLIPLoader, TextGenerateLTX2Prompt, ComfySwitchNode, easy showAnything, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, SaveVideo, VAEDecodeTiled]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `LTXVDualCFGGuider`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`LTXVDualCFGGuider`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`SamplerCustomAdvanced`、`ResolutionSelector`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVConditioning`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`UNETLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`SaveVideo`、`VAEDecodeTiled`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
