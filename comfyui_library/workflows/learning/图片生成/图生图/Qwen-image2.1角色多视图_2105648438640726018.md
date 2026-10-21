---
key: 图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json
name: Qwen-image2.1角色多视图_2105648438640726018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json
hash: 0ca8aa9cad24bd05
coverage: 0.857143
learned_at: 2026-10-21 00:43:31
nodes: [CLIPLoader, VAELoader, UNETLoader, Anything Everywhere3, ResolutionSelector, KSampler, EmptyLatentImage, VAEDecode, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, TextEncodeQwenImage21, LoadImage, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9527, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `ResolutionSelector`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `9527`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ResolutionSelector`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
