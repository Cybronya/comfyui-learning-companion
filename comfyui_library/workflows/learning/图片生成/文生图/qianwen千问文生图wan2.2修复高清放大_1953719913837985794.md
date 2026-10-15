---
key: 图片生成/文生图/qianwen千问文生图wan2.2修复高清放大_1953719913837985794.json
name: qianwen千问文生图wan2.2修复高清放大_1953719913837985794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qianwen千问文生图wan2.2修复高清放大_1953719913837985794.json
hash: 87298000c05bacfa
coverage: 0.863636
learned_at: 2026-10-10 20:59:23
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, VAEEncode, Reroute, VAEDecode, ImageUpscaleWithModel, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, Image Tiled, ImageConcanateOfUtils, ImageFromBatch, ImageFromBatch, PreviewImage, UpscaleModelLoader, UNETLoader, VAELoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, LoraLoader, LoraLoader, KSampler, ImageConcanateOfUtils, ImageConcanateOfUtils, CLIPTextEncode, CLIPTextEncode, LoraLoader, SaveImage, Image Comparer (rgthree), VAEDecode, EmptySD3LatentImage, CLIPTextEncode, UNETLoader, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, Reroute, CR Text, CLIPLoader]
patterns: [lora]
missing: [CR Text, Image Tiled]
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 722313145982736, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/qianwen千问文生图wan2.2修复高清放大_1953719913837985794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qianwen千问文生图wan2.2修复高清放大_1953719913837985794.json`

## 结构

**节点**（44 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `VAEEncode`
- `Reroute`
- `VAEDecode`
- `ImageUpscaleWithModel`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageFromBatch`
- `PreviewImage`
- `UpscaleModelLoader`
- `UNETLoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `LoraLoader`
- `LoraLoader`
- `KSampler`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoraLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode`
- `EmptySD3LatentImage`
- `CLIPTextEncode`
- `UNETLoader`
- `KSampler`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `Reroute`
- `CR Text`
- `CLIPLoader`

**识别到的模式**：lora

## 关键参数

- `cfg` = `3.5`
- `denoise` = `1`
- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `722313145982736`
- `steps` = `20`
- `strength_clip` = `0.7000000000000002`
- `strength_model` = `0.7000000000000002`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`VAEEncode`、`Reroute`、`VAEDecode`、`ImageUpscaleWithModel`、`ImageFromBatch`、`Image Tiled`、`ImageConcanateOfUtils`、`PreviewImage`、`UpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ImageScaleToTotalPixels`、`LoraLoader`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`Image Comparer (rgthree)`、`EmptySD3LatentImage`

**缺卡**（2）：`CR Text`、`Image Tiled`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识
