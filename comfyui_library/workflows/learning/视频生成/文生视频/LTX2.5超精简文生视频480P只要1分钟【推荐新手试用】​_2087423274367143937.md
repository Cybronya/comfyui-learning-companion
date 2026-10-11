---
key: 视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json
name: LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json
hash: 0215b6786e8dc1fd
coverage: 0.85
learned_at: 2026-10-11 20:53:38
nodes: [LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, RandomNoise, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveInt, MarkdownNote, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAELoader, VAELoader, LatentUpscaleModelLoader, CreateVideo, SamplerCustomAdvanced, SaveVideo, KSamplerSelect, ResolutionSelector, CLIPTextEncode, UNETLoader, CLIPTextEncode, CLIPLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`VAELoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
