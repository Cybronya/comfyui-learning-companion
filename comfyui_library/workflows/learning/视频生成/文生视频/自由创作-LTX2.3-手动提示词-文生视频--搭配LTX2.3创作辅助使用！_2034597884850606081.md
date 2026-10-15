---
key: 视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json
name: 自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json
hash: e6175f46060cd079
coverage: 0.822222
learned_at: 2026-10-15 22:49:00
nodes: [LTXVAudioVAELoader, CLIPTextEncode, PreviewAny, CFGGuider, LTXVScheduler, LTXVCropGuides, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, CreateVideo, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, RandomNoise, VAEDecodeTiled, VAEDecode, LTXVAudioVAEDecode, DualCLIPLoader, PrimitiveInt, PrimitiveFloat, ImageScaleBy, GetImageSize, SaveVideo, LoraLoaderModelOnly, CheckpointLoaderSimple, Note, Note, LTXAVTextEncoderLoader, RH_LLMAPI_Pro_Node, easy showAnything, EmptyImage, CR Prompt Text, CR Prompt Text, TextGenerateLTX2Prompt, CR Prompt Text, PrimitiveInt, LoraLoaderModelOnly, CLIPTextEncode, EmptyLTXVLatentVideo, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 259213581619276, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `CFGGuider`
- `LTXVScheduler`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveFloat`
- `ImageScaleBy`
- `GetImageSize`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `LTXAVTextEncoderLoader`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `EmptyImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `Note`

## 关键参数

- `seed` = `259213581619276`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`LTXVAudioVAELoader`、`CLIPTextEncode`、`CFGGuider`、`LTXVScheduler`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`KSampler`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConditioning`、`RandomNoise`、`VAEDecodeTiled`、`VAEDecode`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`ImageScaleBy`、`GetImageSize`、`SaveVideo`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`RH_LLMAPI_Pro_Node`、`EmptyImage`、`CR Prompt Text`、`TextGenerateLTX2Prompt`、`EmptyLTXVLatentVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
