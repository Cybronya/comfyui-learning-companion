---
key: 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json
name: LTX2.3-全自动提示词-文生视频_2070775557209546753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json
hash: 5aa2f742a70e5ceb
coverage: 0.843137
learned_at: 2026-10-15 22:45:03
nodes: [LTXVAudioVAELoader, CLIPTextEncode, PreviewAny, CFGGuider, LTXVScheduler, LTXVCropGuides, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, CreateVideo, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, RandomNoise, VAEDecodeTiled, VAEDecode, LTXVAudioVAEDecode, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, SaveVideo, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CLIPTextEncode, PrimitiveFloat, LTXVEmptyLatentAudio, ImageScaleBy, PrimitiveInt, CM_IntToFloat, PrimitiveInt, easy int, easy int, SimpleMath+, Note, LatentUpscaleModelLoader, TextGenerateLTX2Prompt, CR Prompt Text, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, CR Prompt Text, llama_cpp_parameters, Note, Note, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 45569171916750, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-全自动提示词-文生视频_2070775557209546753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
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
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `PrimitiveInt`
- `CM_IntToFloat`
- `PrimitiveInt`
- `easy int`
- `easy int`
- `SimpleMath+`
- `Note`
- `LatentUpscaleModelLoader`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `CR Prompt Text`
- `llama_cpp_parameters`
- `Note`
- `Note`
- `CR Prompt Text`

## 关键参数

- `seed` = `45569171916750`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`LTXVAudioVAELoader`、`CLIPTextEncode`、`CFGGuider`、`LTXVScheduler`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`KSampler`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConditioning`、`RandomNoise`、`VAEDecodeTiled`、`VAEDecode`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`EmptyImage`、`EmptyLTXVLatentVideo`、`GetImageSize`、`SaveVideo`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`CM_IntToFloat`、`easy int`、`SimpleMath+`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
