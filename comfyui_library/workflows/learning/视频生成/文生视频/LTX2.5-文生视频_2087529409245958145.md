---
key: 视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json
name: LTX2.5-文生视频_2087529409245958145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json
hash: d38b44bcad88c1f8
coverage: 0.833333
learned_at: 2026-10-11 20:53:38
nodes: [LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, VHS_VideoCombine, ManualSigmas, TextGenerateLTX2Prompt, PrimitiveInt, PrimitiveInt, CLIPLoader, MarkdownNote, LTXVEmptyLatentAudio, LTXVLatentUpsampler, EmptyLTXVLatentVideo, LTXVConcatAVLatent, PrimitiveInt, ResolutionSelector, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveStringMultiline, easy showAnything, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（42 个）：
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `ManualSigmas`
- `TextGenerateLTX2Prompt`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `MarkdownNote`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVLatentUpsampler` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `RandomNoise`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`LTXVConditioning`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`ResolutionSelector`、`ComfyMathExpression`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
