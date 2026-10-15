---
key: 视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json
name: LTX2.5文生视频-高质量直出1K_2087559289287303170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json
hash: bf6befe9c6e55a52
coverage: 0.833333
learned_at: 2026-10-15 22:45:17
nodes: [ComfyMathExpression, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, RandomNoise, ComfyMathExpression, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, LTXVAudioVAEDecode, LTXVLatentUpsampler, VAELoader, VAELoader, SamplerCustomAdvanced, LTXVDualCFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, CLIPTextEncode, PrimitiveInt, LTXVSeparateAVLatent, CLIPTextEncode, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, PrimitiveInt, ResolutionSelector, PrimitiveInt, PrimitiveInt, SaveVideo, CLIPLoader, LatentUpscaleModelLoader, MarkdownNote, MarkdownNote, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `ComfyMathExpression`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVDualCFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`ComfyMathExpression`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`VAELoader`、`LTXVConditioning`、`CLIPTextEncode`、`ResolutionSelector`、`SaveVideo`、`CLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
