---
key: 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json
name: Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json
hash: 0b321ddbf2dd575b
coverage: 0.782609
learned_at: 2026-10-26 22:03:15
nodes: [CLIPLoader, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAELoader, UNETLoader, SaveImage, TextGenerateLTX2Prompt, CLIPLoader, easy showAnything, BatchImagesNode, LoadImage, TextEncodeQwenImage21, MarkdownNote, CR Text, LoadImage, LoadImage, LoadImage, VAEDecode, ResolutionSelector, MarkdownNote, 孤海注释, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 373755065265657, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `easy showAnything`
- `BatchImagesNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `孤海注释`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `373755065265657`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`SaveImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`LoadImage`、`TextEncodeQwenImage21`、`CR Text`、`VAEDecode`、`ResolutionSelector`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
