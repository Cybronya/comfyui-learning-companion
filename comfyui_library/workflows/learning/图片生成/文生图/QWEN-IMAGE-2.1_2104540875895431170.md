---
key: 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json
name: QWEN-IMAGE-2.1_2104540875895431170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json
hash: c9581c8119eabab9
coverage: 0.923077
learned_at: 2026-10-10 20:58:49
nodes: [SaveImage, VAEDecode, KSampler, LoadImage, QwenImage21Cache, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, EmptyLatentImage, ComfySwitchNode, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1624, "sampler_name": "euler", "scheduler": "simple", "seed": 980875041290279, "steps": 25, "width": 1080}
---

# 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json`

## 结构

**节点**（13 个）：
- `SaveImage`
- `VAEDecode`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `UNETLoader`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1624`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `980875041290279`
- `steps` = `25`
- `width` = `1080`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ComfySwitchNode`
