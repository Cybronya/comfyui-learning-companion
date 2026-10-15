---
key: 视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json
name: 🦖LTX2.0文生视频_2008714720701849601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json
hash: 14ce10fb177c7631
coverage: 0.826087
learned_at: 2026-10-15 22:49:14
nodes: [LTXVScheduler, LTXAVTextEncoderLoader, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, SamplerCustomAdvanced, Reroute, CreateVideo, PrimitiveNode, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, KSamplerSelect, MarkdownNote, MarkdownNote, CLIPTextEncode, SaveVideo, EmptyImage, ImageScaleBy, GetImageSize, MathExpression|pysssss, PrimitiveInt, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `CreateVideo`
- `PrimitiveNode`
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `JWInteger`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（38/46）

**有卡**：`LTXVScheduler`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVAudioVAELoader`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSamplerSelect`、`SaveVideo`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`MathExpression|pysssss`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
