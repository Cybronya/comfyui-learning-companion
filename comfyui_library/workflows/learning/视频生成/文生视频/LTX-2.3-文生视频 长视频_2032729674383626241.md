---
key: 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json
name: LTX-2.3-文生视频 长视频_2032729674383626241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json
hash: 67e5b76c558eecea
coverage: 0.842105
learned_at: 2026-10-15 22:44:41
nodes: [LTXVScheduler, LatentUpscaleModelLoader, ImageScaleBy, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, CreateVideo, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, MarkdownNote, KSamplerSelect, Reroute, CheckpointLoaderSimple, LTXVAudioVAELoader, KSampler, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVCropGuides, SaveVideo, LTXAVTextEncoderLoader, LoraLoaderModelOnly, DualCLIPLoader, RandomNoise, GetImageSize, PreviewAny, EmptyImage, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PrimitiveInt, PrimitiveInt, CLIPTextEncode, TextGenerateLTX2Prompt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 37921308273519, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LTXVScheduler`
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `SaveVideo`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `RandomNoise`
- `GetImageSize`
- `PreviewAny`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `37921308273519`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`LTXVScheduler`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVConditioning`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CFGGuider`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`KSampler`、`LTXVCropGuides`、`SaveVideo`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`RandomNoise`、`GetImageSize`、`EmptyImage`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
