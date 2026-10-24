---
key: 图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json
name: doubao-seed-2+zimage-turbo模特文生图_2072582582184796162
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json
hash: 85e8cc562693f3d5
coverage: 0.805556
learned_at: 2026-10-23 11:34:38
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, easy cleanGpuUsed, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageConcatMulti, ImageConcatMulti, ImageConcatMulti, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), String Literal, CR Prompt List, easy showAnything, ImpactInt, ImpactInt, EmptyLatentImage, CLIPTextEncode, VAELoader, CLIPLoader, KSampler, easy showAnything, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Batch Images From List, RH_LLMAPI_Pro_Node, CR Text, CR Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.1, "denoise": 1, "height": 1280, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 581493387965875, "steps": 10, "width": 720}
---

# 图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `String Literal`
- `CR Prompt List`
- `easy showAnything`
- `ImpactInt`
- `ImpactInt`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Batch Images From List`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `581493387965875`
- `steps` = `10`
- `cfg` = `1.1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`easy cleanGpuUsed`、`ImageFromBatch`、`ImageConcatMulti`、`LoadImage`、`String Literal`、`CR Prompt List`、`ImpactInt`、`EmptyLatentImage`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Batch Images From List`、`RH_LLMAPI_Pro_Node`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
