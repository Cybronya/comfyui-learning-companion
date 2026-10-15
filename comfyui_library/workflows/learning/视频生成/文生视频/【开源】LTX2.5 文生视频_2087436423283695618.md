---
key: 视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json
name: 【开源】LTX2.5 文生视频_2087436423283695618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json
hash: 2e2c16237a03ce67
coverage: 0.875
learned_at: 2026-10-15 22:47:41
nodes: [LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVDualCFGGuider, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, LTXVConditioning, LTXVLatentUpsampler, RandomNoise, LTXVAudioVAEDecode, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, UNETLoader, LatentUpscaleModelLoader, ManualSigmas, CreateVideo, SaveVideo, MarkdownNote, Text, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VAELoader, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPLoader, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, PrimitiveInt, ResolutionSelector, VAELoader, VAEDecodeTiled]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVDualCFGGuider`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `Text`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `ResolutionSelector`
- `VAELoader`
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVConcatAVLatent`、`ManualSigmas`、`UNETLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`SaveVideo`、`Text`、`ComfyMathExpression`、`VAELoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPLoader`、`ResolutionSelector`、`VAEDecodeTiled`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
