---
key: 图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json
name: image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json
hash: 00b31765b06cb0c9
coverage: 0.8125
learned_at: 2026-10-21 00:45:31
nodes: [MarkdownNote, ResolutionSelector, CLIPLoader, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, KSampler, UNETLoader, LoraLoaderModelOnly, MarkdownNote, Note, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 353910297830868, "steps": 25, "width": 1024}
---

# 图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `Note`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `353910297830868`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`ResolutionSelector`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
