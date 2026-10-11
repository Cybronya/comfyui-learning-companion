---
key: 视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json
name: ltx2.3文生视频工作流-官方版_2055854688318304257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json
hash: 98e573054bf14ca6
coverage: 0.782609
learned_at: 2026-10-11 19:49:44
nodes: [ManualSigmas, CFGGuider, GetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, PrimitiveInt, PrimitiveFloat, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, GetImageSize, ImageScaleBy, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConditioning, LTXVConcatAVLatent, Reroute, CFGGuider, KSamplerSelect, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVCropGuides, LTXVConcatAVLatent, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, VAEDecode, CreateVideo, SetNode, EmptyImage, PrimitiveInt, MarkdownNote, LTXAVTextEncoderLoader, SaveVideo, PrimitiveStringMultiline, MarkdownNote, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `ManualSigmas`
- `CFGGuider`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SetNode`
- `EmptyImage`
- `PrimitiveInt`
- `MarkdownNote`
- `LTXAVTextEncoderLoader`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`ManualSigmas`、`CFGGuider`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`GetImageSize`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VAEDecode`、`CreateVideo`、`EmptyImage`、`LTXAVTextEncoderLoader`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
