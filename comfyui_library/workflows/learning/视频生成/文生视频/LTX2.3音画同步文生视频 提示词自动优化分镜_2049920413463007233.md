---
key: 视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json
name: LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json
hash: 932a15f3fec0677d
coverage: 0.818182
learned_at: 2026-10-15 22:45:15
nodes: [CheckpointLoaderSimple, LTXVAudioVAELoader, RandomNoise, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, GetNode, LTXVConditioning, LTXAVTextEncoderLoader, CLIPTextEncode, KSamplerSelect, LTXVScheduler, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, MathExpression|pysssss, LTXVConcatAVLatent, SetNode, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, CR Prompt Text, RH_LLMAPI_Pro_Node, EmptyImage, PrimitiveNode, Int, Int, CR Prompt Text, SetNode, easy showAnything, CLIPTextEncode, SamplerCustomAdvanced, GetNode, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 504402860620645, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `RandomNoise`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTXVConditioning`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `MathExpression|pysssss`
- `LTXVConcatAVLatent`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `EmptyImage`
- `PrimitiveNode`
- `Int`
- `Int`
- `CR Prompt Text`
- `SetNode`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `504402860620645`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`RandomNoise`、`CFGGuider`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVScheduler`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`KSampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`GetImageSize`、`ImageScaleBy`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`EmptyImage`、`Int`、`SamplerCustomAdvanced`、`SaveVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
