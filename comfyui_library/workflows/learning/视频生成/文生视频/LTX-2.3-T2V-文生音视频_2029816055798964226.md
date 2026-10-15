---
key: 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json
name: LTX-2.3-T2V-文生音视频_2029816055798964226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json
hash: 0d65e99fa88a7ef6
coverage: 0.818182
learned_at: 2026-10-15 22:44:40
nodes: [LTXVScheduler, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CLIPTextEncode, PrimitiveInt, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, SamplerCustomAdvanced, CLIPTextEncode, CreateVideo, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, KSamplerSelect, KSamplerSelect, RandomNoise, Reroute, CheckpointLoaderSimple, LTXAVTextEncoderLoader, MarkdownNote, MarkdownNote, SaveVideo, LoraLoaderModelOnly, PreviewAny, EmptyImage, TextGenerateLTX2Prompt, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LTXVScheduler`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `EmptyImage`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVAudioVAELoader`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`SaveVideo`、`LoraLoaderModelOnly`、`EmptyImage`、`TextGenerateLTX2Prompt`、`CR Prompt Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
