---
key: 平台全量/SD3.5+FLUX海报设计_1850861810311196673.json
name: SD3.5+FLUX海报设计_1850861810311196673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SD3.5+FLUX海报设计_1850861810311196673.json
hash: 9c4b77b7b682a920
coverage: 0.861111
learned_at: 2026-11-14 00:56:05
nodes: [TripleCLIPLoader, CLIPTextEncode, CLIPTextEncode, KSampler, Reroute, UnetLoaderGGUF, DualCLIPLoader, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, ImageUpscaleWithModel, VAEEncode, SamplerCustomAdvanced, VAELoader, ConditioningZeroOut, ConditioningSetTimestepRange, ConditioningSetTimestepRange, ConditioningCombine, EmptySD3LatentImage, VAEDecode, Reroute, PreviewImage, CLIPTextEncode, FluxGuidance, LoraLoader, VAEDecode, SaveImage, PreviewImage, CheckpointLoaderSimple, UpscaleModelLoader, ModelSamplingSD3, Label (rgthree), Label (rgthree), Label (rgthree), JjkText]
patterns: [lora]
missing: []
parameters: {"cfg": 5.5200000000000005, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "lora_name": "3D卡通人物_职场人物，卡通肖像_v1.0.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 337308386879242, "steps": 20, "strength_clip": 0.72, "strength_model": 0.4}
---

# 平台全量/SD3.5+FLUX海报设计_1850861810311196673.json

> 来源文件 `comfyui_library/workflows/平台全量/SD3.5+FLUX海报设计_1850861810311196673.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `TripleCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Reroute`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `ConditioningCombine`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Reroute`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `UpscaleModelLoader`
- `ModelSamplingSD3`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `JjkText`

**识别到的模式**：lora

## 关键参数

- `seed` = `337308386879242`
- `steps` = `20`
- `cfg` = `5.5200000000000005`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `lora_name` = `3D卡通人物_职场人物，卡通肖像_v1.0.safetensors`
- `strength_model` = `0.4`
- `strength_clip` = `0.72`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`TripleCLIPLoader`、`CLIPTextEncode`、`KSampler`、`UnetLoaderGGUF`、`DualCLIPLoader`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`ImageUpscaleWithModel`、`VAEEncode`、`SamplerCustomAdvanced`、`VAELoader`、`ConditioningZeroOut`、`ConditioningSetTimestepRange`、`ConditioningCombine`、`EmptySD3LatentImage`、`VAEDecode`、`FluxGuidance`、`LoraLoader`、`SaveImage`、`CheckpointLoaderSimple`、`UpscaleModelLoader`、`ModelSamplingSD3`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、KSamplerSelect
