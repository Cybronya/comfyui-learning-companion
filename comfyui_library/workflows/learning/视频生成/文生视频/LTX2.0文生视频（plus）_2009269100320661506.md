---
key: 视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json
name: LTX2.0文生视频（plus）_2009269100320661506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json
hash: 9fbb3fa5ad2fe8a3
coverage: 0.853659
learned_at: 2026-10-15 22:44:54
nodes: [MarkdownNote, ManualSigmas, LatentUpscaleModelLoader, CFGGuider, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, MarkdownNote, MarkdownNote, CLIPTextEncode, EmptyImage, ImageScaleBy, GetImageSize, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SamplerCustomAdvanced, CFGGuider, LTXVScheduler, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveInt, CreateVideo, PrimitiveFloat, PrimitiveInt, LTXVLatentUpsampler, RandomNoise, RandomNoise, CheckpointLoaderSimple, SaveVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `MarkdownNote`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `CreateVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`ManualSigmas`、`LatentUpscaleModelLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`KSamplerSelect`、`CLIPTextEncode`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVLatentUpsampler`、`RandomNoise`、`CheckpointLoaderSimple`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
