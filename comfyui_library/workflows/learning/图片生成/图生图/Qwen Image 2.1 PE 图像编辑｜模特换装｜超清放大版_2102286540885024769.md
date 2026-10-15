---
key: 图片生成/图生图/Qwen Image 2.1 PE 图像编辑｜模特换装｜超清放大版_2102286540885024769.json
name: Qwen Image 2.1 PE 图像编辑｜模特换装｜超清放大版_2102286540885024769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑｜模特换装｜超清放大版_2102286540885024769.json
hash: dc5b594faab2dee5
coverage: 0.888889
learned_at: 2026-10-15 22:25:11
nodes: [CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, QwenImage21Cache, UNETLoader, ComfySwitchNode, TextEncodeQwenImage21, VAELoader, LoadImage, LoadImage, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, VAEDecode, 忽略多组孤海, 忽略多组孤海, Any Switch (rgthree), KSampler, SeedVR2VideoUpscaler, SaveImage, MuyeTextEditOutput, EmptyLatentImage, ImpactInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1200, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 25, "width": 800}
---

# 图片生成/图生图/Qwen Image 2.1 PE 图像编辑｜模特换装｜超清放大版_2102286540885024769.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑｜模特换装｜超清放大版_2102286540885024769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `Any Switch (rgthree)`
- `KSampler` ★核心
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `MuyeTextEditOutput`
- `EmptyLatentImage` ★核心
- `ImpactInt`

## 关键参数

- `seed` = `19960422`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `800`
- `height` = `1200`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPLoader`、`LoadImage`、`QwenPERewriteT8`、`QwenImage21Cache`、`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEDecode`、`忽略多组孤海`、`KSampler`、`SeedVR2VideoUpscaler`、`SaveImage`、`MuyeTextEditOutput`、`EmptyLatentImage`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、SaveImage、EmptyLatentImage、LoadImage
