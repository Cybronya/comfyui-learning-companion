---
key: 图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json
name: qwen image2.1 加速版三图图生图_2108114179877068802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json
hash: 5740d7233c7a6274
coverage: 0.846154
learned_at: 2026-10-21 00:46:02
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, QwenPERewriteT8, Note, ResizeAndPadImage, LoadImage, ResolutionSelector, LoadImage, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 748457285561669, "steps": 40}
---

# 图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `Note`
- `ResizeAndPadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `748457285561669`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`SeedVR2LoadDiTModel`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`ResizeAndPadImage`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache
