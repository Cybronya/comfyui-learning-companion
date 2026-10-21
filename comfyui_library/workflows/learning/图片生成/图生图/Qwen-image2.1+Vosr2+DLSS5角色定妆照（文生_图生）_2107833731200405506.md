---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107833731200405506.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107833731200405506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107833731200405506.json
hash: e70c9892dbf05713
coverage: 0.866667
learned_at: 2026-10-21 00:43:23
nodes: [CLIPLoader, VAELoader, PrimitiveStringMultiline, UNETLoader, EmptyLatentImage, ClownsharKSampler_Beta, SaveImage, ResolutionSelector, LoadImage, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE, TextEncodeQwenImage21, VAEDecode, WujiCleaner, WujiUpscaler2]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 904, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent", "width": 1560}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107833731200405506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107833731200405506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiUpscaler2`

## 关键参数

- `width` = `1560`
- `height` = `904`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`ClownsharKSampler_Beta`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`RH_LLMAPI_NODE`、`TextEncodeQwenImage21`、`VAEDecode`、`WujiCleaner`、`WujiUpscaler2`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader
