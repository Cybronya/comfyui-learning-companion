---
key: 图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json
name: qwen-image-2.1文生图_2101682733440389121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json
hash: 5d058efe7fd00d72
coverage: 0.923077
learned_at: 2026-10-20 01:51:56
nodes: [KSampler, CLIPLoader, UNETLoader, VAELoader, Note, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, VAEDecode, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 553880675634271, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `553880675634271`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`KSampler`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
