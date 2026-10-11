---
key: 视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json
name: LTX2.5文生视频_2087539582974906369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json
hash: ebfd598740cffe85
coverage: 0.857143
learned_at: 2026-10-11 20:53:38
nodes: [PrimitiveBoolean, CLIPLoader, TextGenerateLTX2Prompt, ComfySwitchNode, PreviewAny, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVDualCFGGuider, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, RandomNoise, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, RandomNoise, SaveVideo, PrimitiveInt, LoraLoaderModelOnly, UNETLoader, MarkdownNote, KSamplerSelect, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `PrimitiveBoolean`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PreviewAny`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `RandomNoise`
- `SaveVideo`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`PrimitiveBoolean`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`VAELoader`、`LatentUpscaleModelLoader`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVDualCFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`KSamplerSelect`、`ResolutionSelector`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
