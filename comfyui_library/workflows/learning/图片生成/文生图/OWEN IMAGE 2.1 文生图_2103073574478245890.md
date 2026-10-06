---
key: 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json
name: OWEN IMAGE 2.1 文生图_2103073574478245890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json
hash: 5835dbddc3e7aa29
coverage: 0.769231
learned_at: 2026-10-07 02:13:02
nodes: [VAEDecode, TextEncodeQwenImage21, EmptyLatentImage, PrimitiveStringMultiline, ResolutionSelector, MarkdownNote, KSampler, VAELoader, CLIPLoader, UNETLoader, PrimitiveStringMultiline, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 398153285210536, "steps": 25, "width": 1024}
---

# 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MarkdownNote`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `398153285210536`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`KSampler`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
