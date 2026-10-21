---
key: 图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json
name: Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json
hash: 4f2fd5ef821fb1a1
coverage: 0.842105
learned_at: 2026-10-21 00:42:15
nodes: [CLIPLoader, VAELoader, UNETLoader, LoadImage, LoadImage, LoadImage, QwenImage21Cache, KSampler, VAEDecode, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, EmptyLatentImage, SaveImage, 忽略多组孤海, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2000, "sampler_name": "euler", "scheduler": "simple", "seed": 1111988862895067, "steps": 25, "width": 1600}
---

# 图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `忽略多组孤海`
- `MarkdownNote`

## 关键参数

- `seed` = `1111988862895067`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1600`
- `height` = `2000`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`SaveImage`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
