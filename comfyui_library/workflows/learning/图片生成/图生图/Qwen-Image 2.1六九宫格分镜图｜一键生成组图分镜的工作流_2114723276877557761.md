---
key: 图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json
name: Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json
hash: eccb938f8843681e
coverage: 0.820513
learned_at: 2026-10-30 17:50:58
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, KSampler, VAEDecode, TTP_Image_Tile_Batch, PrimitiveStringMultiline, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageResizeKJv2, easy mathInt, easy mathInt, SaveImage, easy mathInt, easy mathInt, PrimitiveStringMultiline, easy imageSwitch, ComfySwitchNode, easy boolean, easy mathInt, easy mathInt, ComfySwitchNode, ImageRemoveAlpha+, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoadImage, SaveImage, ResolutionSelector, VOSR2Upscale, VOSR2ModelLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1102399595550366, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Tile_Batch`
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageResizeKJv2`
- `easy mathInt`
- `easy mathInt`
- `SaveImage`
- `easy mathInt`
- `easy mathInt`
- `PrimitiveStringMultiline`
- `easy imageSwitch`
- `ComfySwitchNode`
- `easy boolean`
- `easy mathInt`
- `easy mathInt`
- `ComfySwitchNode`
- `ImageRemoveAlpha+`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `ResolutionSelector`
- `VOSR2Upscale`
- `VOSR2ModelLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1102399595550366`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`ImageResizeKJv2`、`easy mathInt`、`SaveImage`、`easy imageSwitch`、`easy boolean`、`ImageRemoveAlpha+`、`ResolutionSelector`、`VOSR2Upscale`、`VOSR2ModelLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
