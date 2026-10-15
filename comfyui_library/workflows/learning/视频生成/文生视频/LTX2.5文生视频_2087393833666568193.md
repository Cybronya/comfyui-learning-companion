---
key: 视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json
name: LTX2.5文生视频_2087393833666568193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json
hash: 1cf13b5a17d1e6ae
coverage: 0.840909
learned_at: 2026-10-15 22:45:17
nodes: [LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, RandomNoise, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, SaveVideo, CreateVideo, ManualSigmas, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveInt, ResolutionSelector, CLIPLoader, PreviewAny, TextGenerateLTX2Prompt, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
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
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `CreateVideo`
- `ManualSigmas`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `ResolutionSelector`
- `CLIPLoader`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`SaveVideo`、`CreateVideo`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
