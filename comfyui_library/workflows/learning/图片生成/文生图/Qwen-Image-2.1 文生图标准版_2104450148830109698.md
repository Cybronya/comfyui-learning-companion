---
key: 图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json
name: Qwen-Image-2.1 文生图标准版_2104450148830109698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json
hash: 0096b11770cecf8f
coverage: 0.769231
learned_at: 2026-10-07 02:24:46
nodes: [KSampler, CR Text, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextEncodeQwenImage21, QwenImage21Cache, MarkdownNote, ResolutionSelector, VAEDecode, SaveImage]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `CR Text`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `MarkdownNote`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`ResolutionSelector`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
