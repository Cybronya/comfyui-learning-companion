---
key: 图片生成/图生图/生图-图放大-VOSR 2.0_2097354360434020354.json
name: 生图-图放大-VOSR 2.0_2097354360434020354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-图放大-VOSR 2.0_2097354360434020354.json
hash: 33687ca9d32d183f
coverage: 0.8
learned_at: 2026-10-21 00:55:07
nodes: [Image Comparer (rgthree), ImageConcanate, SaveImage, GetImageSizeAndCount, PreviewImage, Int, VOSR2ModelLoader, VOSR2Upscale, LoadImage, GetImageSizeAndCount]
patterns: []
missing: []
---

# 图片生成/图生图/生图-图放大-VOSR 2.0_2097354360434020354.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-图放大-VOSR 2.0_2097354360434020354.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（10 个）：
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImage`
- `GetImageSizeAndCount`
- `PreviewImage`
- `Int`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `LoadImage`
- `GetImageSizeAndCount`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`ImageConcanate`、`SaveImage`、`GetImageSizeAndCount`、`Int`、`VOSR2ModelLoader`、`VOSR2Upscale`、`LoadImage`

**用到的条目**：LoadImage、VOSR2Upscale、GetImageSizeAndCount、SaveImage、ImageConcanate、Int、VOSR2ModelLoader、sdxl_portrait_controlnet_lora_sampler
