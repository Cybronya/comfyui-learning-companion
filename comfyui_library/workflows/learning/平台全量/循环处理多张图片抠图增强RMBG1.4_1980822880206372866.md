---
key: 平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json
name: 循环处理多张图片抠图增强RMBG1.4_1980822880206372866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json
hash: 2db2e4945c876507
coverage: 0.730769
learned_at: 2026-11-14 02:04:01
nodes: [easy showAnything, PreviewImage, easy forLoopStart, easy imageCount, RHBatchImages:, VAEEncode, CLIPTextEncode, CLIPTextEncode, PreviewImage, Bjornulf_ShowInt, easy forLoopEnd, CheckpointLoaderSimple, BNK_TiledKSampler, LayerColor: Brightness & Contrast, RHExtractImage, PreviewImage, VAEDecode, PreviewImage, SaveImage, Upscale Model Loader, RHExtractImage, ImageUpscaleWithModel, RHUploadZip, easy imageRemBg, Image Comparer (rgthree), Reroute]
patterns: []
missing: []
parameters: {"cfg": 1024, "checkpoint": "maximumEffort_maximumEffortXLV10.safetensors", "denoise": 8, "sampler_name": "random", "scheduler": 28, "seed": 1055936316635400, "steps": 1024}
---

# 平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json

> 来源文件 `comfyui_library/workflows/平台全量/循环处理多张图片抠图增强RMBG1.4_1980822880206372866.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `easy showAnything`
- `PreviewImage`
- `easy forLoopStart`
- `easy imageCount`
- `RHBatchImages:`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Bjornulf_ShowInt`
- `easy forLoopEnd`
- `CheckpointLoaderSimple` ★核心
- `BNK_TiledKSampler` ★核心
- `LayerColor: Brightness & Contrast`
- `RHExtractImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `Upscale Model Loader`
- `RHExtractImage`
- `ImageUpscaleWithModel`
- `RHUploadZip`
- `easy imageRemBg`
- `Image Comparer (rgthree)`
- `Reroute`

## 关键参数

- `checkpoint` = `maximumEffort_maximumEffortXLV10.safetensors`
- `seed` = `1055936316635400`
- `steps` = `1024`
- `cfg` = `1024`
- `sampler_name` = `random`
- `scheduler` = `28`
- `denoise` = `8`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`easy forLoopStart`、`easy imageCount`、`RHBatchImages:`、`VAEEncode`、`CLIPTextEncode`、`Bjornulf_ShowInt`、`easy forLoopEnd`、`CheckpointLoaderSimple`、`BNK_TiledKSampler`、`LayerColor: Brightness & Contrast`、`RHExtractImage`、`VAEDecode`、`SaveImage`、`Upscale Model Loader`、`ImageUpscaleWithModel`、`RHUploadZip`、`easy imageRemBg`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、BNK_TiledKSampler、VAEEncode、ImageUpscaleWithModel、Upscale Model Loader、SaveImage
