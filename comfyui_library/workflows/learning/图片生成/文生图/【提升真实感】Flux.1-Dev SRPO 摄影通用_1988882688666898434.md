---
key: 图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json
name: 【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json
hash: fdce155648eced81
coverage: 0.809524
learned_at: 2026-10-10 20:59:31
nodes: [UNETLoader, VAELoader, DualCLIPLoader, ChinesePrompt_Mix, VAEEncode, UpscaleModelLoader, easy cleanGpuUsed, ImageUpscaleWithModel, PreviewImage, LoraLoaderModelOnly, LoadImage, DyPE_FLUX, VAEDecode, Image Comparer (rgthree), CLIPTextEncode, ConditioningZeroOut, FluxGuidance, LoraLoaderModelOnly, ImageResize+, SaveImage, KSampler]
patterns: [image_to_image]
missing: [easy cleanGpuUsed, ImageResize+]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 1, "steps": 20}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json`

## 结构

**节点**（21 个）：
- `UNETLoader`
- `VAELoader`
- `DualCLIPLoader`
- `ChinesePrompt_Mix`
- `VAEEncode`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `LoadImage`
- `DyPE_FLUX`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `LoraLoaderModelOnly`
- `ImageResize+`
- `SaveImage`
- `KSampler`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `0.30000000000000004`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `seed` = `1`
- `steps` = `20`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`ChinesePrompt_Mix`、`VAEEncode`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`PreviewImage`、`LoraLoaderModelOnly`、`LoadImage`、`DyPE_FLUX`、`VAEDecode`、`Image Comparer (rgthree)`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxGuidance`

**缺卡**（2）：`easy cleanGpuUsed`、`ImageResize+`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
