---
key: 图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json
name: qwen_image_2.1图像编辑_2103699751001747458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json
hash: a1db3e9110ce86ed
coverage: 0.714286
learned_at: 2026-10-21 00:46:21
nodes: [UNETLoader, CLIPLoader, MarkdownNote, EmptyLatentImage, VAELoader, KSampler, EmptyImage, ImageResizeKJv2, ImageCompositeMasked, PreviewImage, TextEncodeQwenImage21, VAEDecode, SaveImage, MarkdownNote, MarkdownNote, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, RH_LLMAPI_Pro_Node, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 217871708811924, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `EmptyImage`
- `ImageResizeKJv2`
- `ImageCompositeMasked`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `217871708811924`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`EmptyImage`、`ImageResizeKJv2`、`ImageCompositeMasked`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
