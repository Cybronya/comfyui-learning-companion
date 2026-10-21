---
key: 图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json
name: qwen image2.1 加速版双图图生图_2108108729798455297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json
hash: 329daa641dd915df
coverage: 0.84
learned_at: 2026-10-21 00:46:03
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, QwenPERewriteT8, Note, ResizeAndPadImage, LoadImage, ResolutionSelector, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 11878847723376, "steps": 40}
---

# 图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json`

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
- `Note`
- `ResizeAndPadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `11878847723376`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`SeedVR2LoadDiTModel`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`ResizeAndPadImage`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、QwenImage21Cache
