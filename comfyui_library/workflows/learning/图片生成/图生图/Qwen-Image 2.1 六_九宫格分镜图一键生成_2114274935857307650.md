---
key: 图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json
name: Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json
hash: d8d0a01f6c0a3d21
coverage: 0.744186
learned_at: 2026-10-26 22:03:19
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, MarkdownNote, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, KSampler, VAEDecode, TTP_Image_Tile_Batch, PrimitiveStringMultiline, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageResizeKJv2, easy mathInt, easy mathInt, SaveImage, easy mathInt, easy mathInt, PrimitiveStringMultiline, easy imageSwitch, ComfySwitchNode, easy boolean, easy mathInt, easy mathInt, ComfySwitchNode, MarkdownNote, MarkdownNote, ImageRemoveAlpha+, PrimitiveStringMultiline, MarkdownNote, PrimitiveStringMultiline, LoadImage, LoadImage, SaveImage, ResolutionSelector, VOSR2Upscale, VOSR2ModelLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1102399595550366, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `MarkdownNote`
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
- `MarkdownNote`
- `MarkdownNote`
- `ImageRemoveAlpha+`
- `PrimitiveStringMultiline`
- `MarkdownNote`
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

覆盖率 **74%**（32/43）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`ImageResizeKJv2`、`easy mathInt`、`SaveImage`、`easy imageSwitch`、`easy boolean`、`ImageRemoveAlpha+`、`ResolutionSelector`、`VOSR2Upscale`、`VOSR2ModelLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
