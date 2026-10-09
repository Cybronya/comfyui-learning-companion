---
key: 图片生成/图生图/Qwen2.1 抠图_2101886414299426818.json
name: Qwen2.1 抠图_2101886414299426818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 抠图_2101886414299426818.json
hash: 9e597729b3f5e1b6
coverage: 0.8125
learned_at: 2026-10-09 22:27:07
nodes: [CLIPLoader, VAELoader, MarkdownNote, Note, QwenImage21Cache, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, LoadImage, ResolutionSelector, UNETLoader, LoadImage, ImageScale, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 433015825943053, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen2.1 抠图_2101886414299426818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101886414299426818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `Note`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageScale`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `433015825943053`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`LoadImage`、`ResolutionSelector`、`UNETLoader`、`ImageScale`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
