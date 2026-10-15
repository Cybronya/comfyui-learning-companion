---
key: 视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json
name: LTXV2.0文生视频_2008464606221574146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json
hash: 16323a24e432c096
coverage: 0.782609
learned_at: 2026-10-15 22:45:18
nodes: [MarkdownNote, MarkdownNote, SaveVideo, LTXVScheduler, ManualSigmas, LTXVCropGuides, CFGGuider, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CLIPTextEncode, EmptyImage, PrimitiveInt, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, CLIPTextEncode, CreateVideo, PrimitiveNode, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, KSamplerSelect, MarkdownNote, MarkdownNote, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTXVLatentUpsampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `LTXVScheduler`
- `ManualSigmas`
- `LTXVCropGuides`
- `CFGGuider`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`SaveVideo`、`LTXVScheduler`、`ManualSigmas`、`LTXVCropGuides`、`CFGGuider`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`EmptyImage`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVAudioVAELoader`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
