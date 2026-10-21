---
key: 图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json
name: image_qwen_image_2_1_character_sheet1_2108024739095728130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json
hash: 0f8d92163bca0abd
coverage: 0.8
learned_at: 2026-10-21 00:45:31
nodes: [MarkdownNote, ResolutionSelector, CLIPLoader, EmptyLatentImage, VAELoader, UNETLoader, MarkdownNote, Note, LoraLoaderModelOnly, TextEncodeQwenImage21, KSampler, LoadImage, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 250951929401428, "steps": 25, "width": 1024}
---

# 图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `250951929401428`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`ResolutionSelector`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
