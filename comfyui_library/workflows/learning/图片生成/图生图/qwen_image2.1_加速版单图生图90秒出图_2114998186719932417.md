---
key: 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json
name: qwen_image2.1_加速版单图生图90秒出图_2114998186719932417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json
hash: b29825f3c3720c69
coverage: 0.84
learned_at: 2026-10-30 17:51:51
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, QwenPERewriteT8, CR Prompt Text, LoadImage, ResolutionSelector, ResizeAndPadImage, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 969106663078444, "steps": 40}
---

# 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `LoadImage`
- `ResolutionSelector`
- `ResizeAndPadImage`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `969106663078444`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`SeedVR2LoadDiTModel`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`CR Prompt Text`、`LoadImage`、`ResolutionSelector`、`ResizeAndPadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache
