---
key: 平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json
name: Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json
hash: 7562cb6be6070d06
coverage: 0.857143
learned_at: 2026-11-14 01:07:59
nodes: [ConditioningZeroOut, EmptyLatentImage, PreviewImage, GenerateNoise, LayerUtility: ImageScaleByAspectRatio V2, GetNode, PrimitiveInt, SetNode, ZImageFunControlnet, VAEDecode, ImageUpscaleWithModel, UpscaleModelLoader, CR Seed, LGNoiseInjectionLatent, KSampler, SaveImage, easy framesEditor, easy sam3ImageSegmentation, MaskPreview, ModelPatchLoader, CLIPLoader, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, VAELoader, easy sam3ModelLoader, LoadImage, LoraLoader]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "lora_name": "巨乳.safetensors", "sampler_name": "dpmpp_2s_ancestral", "scheduler": "bong_tangent", "seed": 410810434996197, "steps": 10, "strength_clip": 1, "strength_model": 2, "width": 1024}
---

# 平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json

> 来源文件 `comfyui_library/workflows/平台全量/Z+image+SAM3.1区域重绘工作流换装换脸换任何区域_2096416468069076993.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `GenerateNoise`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `ZImageFunControlnet`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `CR Seed`
- `LGNoiseInjectionLatent`
- `KSampler` ★核心
- `SaveImage`
- `easy framesEditor`
- `easy sam3ImageSegmentation`
- `MaskPreview`
- `ModelPatchLoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `easy sam3ModelLoader`
- `LoadImage`
- `LoraLoader` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `410810434996197`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2s_ancestral`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `lora_name` = `巨乳.safetensors`
- `strength_model` = `2`
- `strength_clip` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`ConditioningZeroOut`、`EmptyLatentImage`、`GenerateNoise`、`LayerUtility: ImageScaleByAspectRatio V2`、`ZImageFunControlnet`、`VAEDecode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`CR Seed`、`LGNoiseInjectionLatent`、`KSampler`、`SaveImage`、`easy framesEditor`、`easy sam3ImageSegmentation`、`MaskPreview`、`ModelPatchLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`easy sam3ModelLoader`、`LoadImage`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
