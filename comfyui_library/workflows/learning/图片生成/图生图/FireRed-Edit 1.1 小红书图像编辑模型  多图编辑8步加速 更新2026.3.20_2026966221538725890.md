---
key: 图片生成/图生图/FireRed-Edit 1.1 小红书图像编辑模型  多图编辑8步加速 更新2026.3.20_2026966221538725890.json
name: FireRed-Edit 1.1 小红书图像编辑模型  多图编辑8步加速 更新2026.3.20_2026966221538725890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Edit 1.1 小红书图像编辑模型  多图编辑8步加速 更新2026.3.20_2026966221538725890.json
hash: 9a6b400a4351f66e
coverage: 0.7
learned_at: 2026-10-23 10:55:28
nodes: [SeedVR2LoadVAEModel, PreviewImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler, VAEDecode, VAELoader, CLIPLoader, SaveImage, SaveImage, Image Comparer (rgthree), easy cleanGpuUsed, easy int, SeedVR2LoadDiTModel, SaveImage, UNETLoader, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcatMulti, ConditioningZeroOut, TextEncodeQwenImageEditPlusAdvance_lrzjason, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), MuyeTextEditOutput, Note, Note, Note, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 430490097027301, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Edit 1.1 小红书图像编辑模型  多图编辑8步加速 更新2026.3.20_2026966221538725890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Edit 1.1 小红书图像编辑模型  多图编辑8步加速 更新2026.3.20_2026966221538725890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `easy int`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `MuyeTextEditOutput`
- `Note`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `430490097027301`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（28/40）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`SaveImage`、`easy cleanGpuUsed`、`easy int`、`SeedVR2LoadDiTModel`、`UNETLoader`、`KSampler`、`LoadImage`、`ImageConcatMulti`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoraLoaderModelOnly`、`MuyeTextEditOutput`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
