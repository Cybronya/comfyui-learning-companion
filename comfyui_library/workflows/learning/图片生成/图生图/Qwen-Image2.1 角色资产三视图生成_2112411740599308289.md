---
key: 图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json
name: Qwen-Image2.1 角色资产三视图生成_2112411740599308289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json
hash: 0584aa5b0a8cbb33
coverage: 0.772727
learned_at: 2026-10-23 11:17:20
nodes: [CLIPLoader, CLIPLoader, VAELoader, KSampler, SaveImage, LoadImage, VAEDecode, Image Comparer (rgthree), SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, Fast Groups Bypasser (rgthree), MarkdownNote, 孤海注释, SaveImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, CR Prompt Text, UNETLoader, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 222392165968139, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `孤海注释`
- `SaveImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `222392165968139`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`LoadImage`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`ResolutionSelector`、`TextEncodeQwenImage21`、`CR Prompt Text`、`UNETLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
