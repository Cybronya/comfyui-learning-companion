---
key: 视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json
name: LTX2.5-文生视频超快工作流_2087433108160344066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json
hash: 93a1579502c65900
coverage: 0.85
learned_at: 2026-10-11 20:53:38
nodes: [LTXVConditioning, LTXVDualCFGGuider, ComfyMathExpression, LTXVConcatAVLatent, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, CreateVideo, SamplerCustomAdvanced, ResolutionSelector, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVLatentUpsampler, CLIPTextEncode, CLIPTextEncode, ManualSigmas, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVDualCFGGuider, RandomNoise, RandomNoise, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, SaveVideo, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
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
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SaveVideo`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LTXVConditioning`、`LTXVDualCFGGuider`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`KSamplerSelect`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`SamplerCustomAdvanced`、`ResolutionSelector`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
