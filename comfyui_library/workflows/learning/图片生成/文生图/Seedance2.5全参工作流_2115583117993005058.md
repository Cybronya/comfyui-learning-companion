---
key: 图片生成/文生图/Seedance2.5全参工作流_2115583117993005058.json
name: Seedance2.5全参工作流_2115583117993005058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Seedance2.5全参工作流_2115583117993005058.json
hash: 8ea5ef3e34afda69
coverage: 0.888889
learned_at: 2026-10-30 17:55:23
nodes: [ConditioningZeroOut, LoraLoaderModelOnly, UpscaleModelLoader, VAEDecode, ImageUpscaleWithModel, PreviewImage, ImageFromBatch, LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, CLIPLoader, KSampler, SaveImage, CLIPTextEncode, LoraLoaderModelOnly, VAELoader, UNETLoader, EmptyLatentImage, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 2106180193952, "steps": 10, "width": 1440}
---

# 图片生成/文生图/Seedance2.5全参工作流_2115583117993005058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Seedance2.5全参工作流_2115583117993005058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `PreviewImage`
- `ImageFromBatch`
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `2106180193952`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`ConditioningZeroOut`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`VAEDecode`、`ImageUpscaleWithModel`、`ImageFromBatch`、`LayerColor: BrightnessContrastV2`、`CLIPLoader`、`KSampler`、`SaveImage`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
