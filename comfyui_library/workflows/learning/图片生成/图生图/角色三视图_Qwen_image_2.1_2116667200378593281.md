---
key: 图片生成/图生图/角色三视图_Qwen_image_2.1_2116667200378593281.json
name: 角色三视图_Qwen_image_2.1_2116667200378593281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen_image_2.1_2116667200378593281.json
hash: b55da81698b220b4
coverage: 0.857143
learned_at: 2026-11-02 19:14:58
nodes: [KSampler, QwenImage21Cache, VAELoader, UNETLoader, CLIPLoader, VAEDecode, LoadImage, ImageScaleToTotalPixels, TextEncodeQwenImage21, ResolutionSelector, EmptyFlux2LatentImage, ImageScaleToTotalPixels, PreviewImage, INTConstant, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 2412653791642, "steps": 25}
---

# 图片生成/图生图/角色三视图_Qwen_image_2.1_2116667200378593281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen_image_2.1_2116667200378593281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `INTConstant`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `2412653791642`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`KSampler`、`QwenImage21Cache`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`LoadImage`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyFlux2LatentImage`、`INTConstant`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、UNETLoader、CLIPLoader、ResolutionSelector、LoadImage
