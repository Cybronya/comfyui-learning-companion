---
key: 图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json
name: qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json
hash: 40b4f10cd47ba766
coverage: 0.833333
learned_at: 2026-10-21 00:46:03
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, QwenPERewriteT8, CR Prompt Text, Note, LoadImage, ResolutionSelector, ResizeAndPadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 480862308269817, "steps": 40}
---

# 图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `Note`
- `LoadImage`
- `ResolutionSelector`
- `ResizeAndPadImage`

## 关键参数

- `seed` = `480862308269817`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`SeedVR2LoadDiTModel`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`CR Prompt Text`、`LoadImage`、`ResolutionSelector`、`ResizeAndPadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache
