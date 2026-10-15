---
key: 视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json
name: LTX2.5文生视频（速度快、像素高）_2087530677137928194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json
hash: cdef9634b82801ef
coverage: 0.822222
learned_at: 2026-10-15 22:45:17
nodes: [LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveInt, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, ResolutionSelector, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, CreateVideo, SamplerCustomAdvanced, LTXVConcatAVLatent, CLIPLoader, PrimitiveBoolean, ComfySwitchNode, CLIPTextEncode, MarkdownNote, PrimitiveStringMultiline, TextGenerateLTX2Prompt, ManualSigmas, RandomNoise, SaveVideo, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `CLIPLoader`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `ManualSigmas`
- `RandomNoise`
- `SaveVideo`
- `PreviewAny`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
