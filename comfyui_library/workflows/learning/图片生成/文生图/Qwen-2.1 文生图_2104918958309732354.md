---
key: 图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json
name: Qwen-2.1 文生图_2104918958309732354
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json
hash: 19df162c062ba814
coverage: 0.785714
learned_at: 2026-10-15 22:27:08
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), UNETLoader, VAELoader, QwenImage21Cache, VAEDecode, SaveImage, CLIPLoader, CLIPTextEncode, KSampler, EmptyLatentImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 251116427069119, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `251116427069119`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`Label (rgthree)`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、QwenImage21Cache、UNETLoader
