---
key: 图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json
name: image_qwen_image_2_1_edit_anything_ref_2102668719456604161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json
hash: 3b55a49c182885ec
coverage: 0.823529
learned_at: 2026-10-21 00:45:32
nodes: [UNETLoader, CLIPLoader, MarkdownNote, MarkdownNote, EmptyLatentImage, VAELoader, KSampler, ResolutionSelector, EmptyImage, ImageResizeKJv2, ImageCompositeMasked, PreviewImage, TextEncodeQwenImage21, VAEDecode, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 502326896502708, "steps": 25, "width": 1024}
---

# 图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ResolutionSelector`
- `EmptyImage`
- `ImageResizeKJv2`
- `ImageCompositeMasked`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `502326896502708`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`ResolutionSelector`、`EmptyImage`、`ImageResizeKJv2`、`ImageCompositeMasked`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
