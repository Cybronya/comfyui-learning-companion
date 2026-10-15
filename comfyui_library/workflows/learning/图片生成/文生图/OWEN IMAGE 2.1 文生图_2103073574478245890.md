---
key: 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json
name: OWEN IMAGE 2.1 文生图_2103073574478245890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json
hash: 5835dbddc3e7aa29
coverage: 0.769231
learned_at: 2026-10-10 20:58:48
nodes: [VAEDecode, TextEncodeQwenImage21, EmptyLatentImage, PrimitiveStringMultiline, ResolutionSelector, MarkdownNote, KSampler, VAELoader, CLIPLoader, UNETLoader, PrimitiveStringMultiline, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 398153285210536, "steps": 25, "width": 1024}
---

# 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json`

## 结构

**节点**（13 个）：
- `VAEDecode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MarkdownNote`
- `KSampler`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SaveImageAdvanced`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `398153285210536`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`PrimitiveStringMultiline`、`ResolutionSelector`、`MarkdownNote`、`KSampler`、`VAELoader`、`CLIPLoader`、`UNETLoader`
