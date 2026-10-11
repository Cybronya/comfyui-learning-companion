---
key: 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json
name: 内置sd2.0，原生4K 文生视频工作流_2046658693634199553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json
hash: 33be70483df163ba
coverage: 0.818182
learned_at: 2026-10-11 19:49:47
nodes: [LTXVScheduler, LTXAVTextEncoderLoader, ManualSigmas, CFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVAudioVAELoader, CFGGuider, KSamplerSelect, KSamplerSelect, CheckpointLoaderSimple, RandomNoise, CLIPTextEncode, VAEDecodeTiled, VAEDecode, LTXVAudioVAEDecode, MarkdownNote, MarkdownNote, SaveVideo, PrimitiveInt, LoraLoaderModelOnly, LTXVConcatAVLatent, PrimitiveFloat, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVLatentUpsampler, Reroute, CreateVideo, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVConditioning, GetImageSize, ImageScaleBy, EmptyImage, PrimitiveInt, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAELoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `CreateVideo`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `GetImageSize`
- `ImageScaleBy`
- `EmptyImage`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`LTXVScheduler`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`CFGGuider`、`LTXVConcatAVLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAELoader`、`KSamplerSelect`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`VAEDecodeTiled`、`VAEDecode`、`LTXVAudioVAEDecode`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`CreateVideo`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`GetImageSize`、`ImageScaleBy`、`EmptyImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
