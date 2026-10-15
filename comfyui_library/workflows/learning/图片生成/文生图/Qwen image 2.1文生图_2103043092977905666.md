---
key: 图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json
name: Qwen image 2.1文生图_2103043092977905666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json
hash: 27d8f0accd283af1
coverage: 0.764706
learned_at: 2026-10-15 22:27:07
nodes: [EmptyLatentImage, VAELoader, CLIPLoader, SaveImage, Note, Label (rgthree), Label (rgthree), MarkdownNote, MarkdownNote, MarkdownNote, ResolutionSelector, VAEDecode, KSampler, QwenImage21Cache, PathchSageAttentionKJ, TextEncodeQwenImage21, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `PathchSageAttentionKJ`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `43`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`SaveImage`、`Label (rgthree)`、`ResolutionSelector`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`PathchSageAttentionKJ`、`TextEncodeQwenImage21`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
