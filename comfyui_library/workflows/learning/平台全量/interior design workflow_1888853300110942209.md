---
key: 平台全量/interior design workflow_1888853300110942209.json
name: interior design workflow_1888853300110942209
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/interior design workflow_1888853300110942209.json
hash: 33a7a3a1ad95aba9
coverage: 0.863636
learned_at: 2026-11-14 01:12:54
nodes: [TimestepKeyframe, TimestepKeyframe, CheckpointLoaderSimple, AIO_Preprocessor, PreviewImage, ControlNetLoaderAdvanced, PreviewImage, KSampler, ACN_AdvancedControlNetApply, Note, CLIPTextEncode, ScaledSoftMaskedUniversalWeights, EmptyLatentImage, CLIPTextEncode, LoraLoader, ClipInterrogator, VAEDecode, SaveImage, LoadImage, ScaledSoftMaskedUniversalWeights, VAELoader, SDXLPromptStylerAll]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 6.5, "checkpoint": "realisticVisionV30_v30VAE    _realisticVision.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "lora_name": "more_details.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 158820269331053, "steps": 30, "strength_clip": 1, "strength_model": 1, "width": 768}
---

# 平台全量/interior design workflow_1888853300110942209.json

> 来源文件 `comfyui_library/workflows/平台全量/interior design workflow_1888853300110942209.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（22 个）：
- `TimestepKeyframe`
- `TimestepKeyframe`
- `CheckpointLoaderSimple` ★核心
- `AIO_Preprocessor`
- `PreviewImage`
- `ControlNetLoaderAdvanced`
- `PreviewImage`
- `KSampler` ★核心
- `ACN_AdvancedControlNetApply` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `ScaledSoftMaskedUniversalWeights`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `ClipInterrogator`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ScaledSoftMaskedUniversalWeights`
- `VAELoader`
- `SDXLPromptStylerAll`

**识别到的模式**：text_to_image、lora

## 关键参数

- `checkpoint` = `realisticVisionV30_v30VAE    _realisticVision.safetensors`
- `seed` = `158820269331053`
- `steps` = `30`
- `cfg` = `6.5`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `more_details.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`TimestepKeyframe`、`CheckpointLoaderSimple`、`AIO_Preprocessor`、`ControlNetLoaderAdvanced`、`KSampler`、`ACN_AdvancedControlNetApply`、`CLIPTextEncode`、`ScaledSoftMaskedUniversalWeights`、`EmptyLatentImage`、`LoraLoader`、`ClipInterrogator`、`VAEDecode`、`SaveImage`、`LoadImage`、`VAELoader`、`SDXLPromptStylerAll`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ACN_AdvancedControlNetApply
