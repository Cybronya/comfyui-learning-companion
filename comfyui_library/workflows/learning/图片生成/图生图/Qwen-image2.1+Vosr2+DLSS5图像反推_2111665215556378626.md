---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json
name: Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json
hash: 16237ad50bced253
coverage: 0.85
learned_at: 2026-10-23 11:18:21
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, VAELoader, RH_Screenwriter, easy showAnything, SaveImage, VAEDecode, ClownsharKSampler_Beta, PrimitiveStringMultiline, UNETLoader, LoadImage, WujiUpscaler2, TextEncodeQwenImage21, Image Comparer (rgthree), WujiPromptEditor, WujiImagePrompt, easy imageSize, EmptyLatentImage, ImageScaleToTotalPixels]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1024, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent", "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `VAELoader`
- `RH_Screenwriter`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `WujiUpscaler2`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `WujiPromptEditor`
- `WujiImagePrompt`
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`VAELoader`、`RH_Screenwriter`、`SaveImage`、`VAEDecode`、`ClownsharKSampler_Beta`、`UNETLoader`、`LoadImage`、`WujiUpscaler2`、`TextEncodeQwenImage21`、`WujiPromptEditor`、`WujiImagePrompt`、`easy imageSize`、`EmptyLatentImage`、`ImageScaleToTotalPixels`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、ClownsharKSampler_Beta
