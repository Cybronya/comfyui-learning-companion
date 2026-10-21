---
key: 图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json
name: Qwen-2.1cos角色生活自拍_2104713076036689921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json
hash: 3b53325a3b5584c7
coverage: 0.764706
learned_at: 2026-10-21 00:43:05
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), TextEncodeQwenImage21, KSampler, VAEDecode, UNETLoader, CLIPLoader, LoadImage, PreviewAny, AILab_QwenVL, ResolutionSelector, SaveImage, QwenImage21Cache, EmptyLatentImage, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 591380817921780, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-2.1cos角色生活自拍_2104713076036689921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `PreviewAny`
- `AILab_QwenVL`
- `ResolutionSelector`
- `SaveImage`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `VAELoader`

## 关键参数

- `seed` = `591380817921780`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`Label (rgthree)`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`AILab_QwenVL`、`ResolutionSelector`、`SaveImage`、`QwenImage21Cache`、`EmptyLatentImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
