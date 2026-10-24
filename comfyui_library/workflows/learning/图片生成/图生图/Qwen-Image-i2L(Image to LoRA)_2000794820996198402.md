---
key: 图片生成/图生图/Qwen-Image-i2L(Image to LoRA)_2000794820996198402.json
name: Qwen-Image-i2L(Image to LoRA)_2000794820996198402
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-i2L(Image to LoRA)_2000794820996198402.json
hash: 8a19604080345bfd
coverage: 0.815789
learned_at: 2026-10-23 11:17:17
nodes: [RunningHub_ImageQwenI2L_LoraGenerator, CLIPLoader, VAELoader, easy showAnything, ImageScaleToTotalPixels, RepeatImageBatch, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, StringFunction|pysssss, RunningHub_ImageQwenI2L_Loader(Style), easy showAnything, ModelSamplingAuraFlow, UNETLoader, SetUnionControlNetType, ImageScaleToTotalPixels, ConditioningZeroOut, easy cleanGpuUsed, CLIPTextEncode, easy imageConcat, easy imageConcat, SaveImage, easy showAnything, VAEDecode, EmptyLatentImage, easy imageSize, PreviewImage, ControlNetApplyAdvanced, KSampler, LoadImage, easy showAnything, RH_LLMAPI_NODE, RH_LLMAPI_NODE, LoraLoaderModelOnly, LoraLoaderModelOnly, ControlNetLoader, AIO_Preprocessor, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1059541267753394, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-i2L(Image to LoRA)_2000794820996198402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-i2L(Image to LoRA)_2000794820996198402.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `RunningHub_ImageQwenI2L_LoraGenerator`
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `ImageScaleToTotalPixels`
- `RepeatImageBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `StringFunction|pysssss`
- `RunningHub_ImageQwenI2L_Loader(Style)`
- `easy showAnything`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `SetUnionControlNetType`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `SaveImage`
- `easy showAnything`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `easy imageSize`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `LoadImage`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `0.8000000000000002`
- `seed` = `1059541267753394`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`RunningHub_ImageQwenI2L_LoraGenerator`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`RepeatImageBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`StringFunction|pysssss`、`RunningHub_ImageQwenI2L_Loader(Style)`、`ModelSamplingAuraFlow`、`UNETLoader`、`SetUnionControlNetType`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`CLIPTextEncode`、`easy imageConcat`、`SaveImage`、`VAEDecode`、`EmptyLatentImage`、`easy imageSize`、`ControlNetApplyAdvanced`、`KSampler`、`LoadImage`、`RH_LLMAPI_NODE`、`LoraLoaderModelOnly`、`ControlNetLoader`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
