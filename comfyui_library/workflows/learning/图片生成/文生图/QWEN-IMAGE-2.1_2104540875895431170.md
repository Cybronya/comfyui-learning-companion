---
key: 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json
name: QWEN-IMAGE-2.1_2104540875895431170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json
hash: c9581c8119eabab9
coverage: 0.923077
learned_at: 2026-10-07 02:25:01
nodes: [SaveImage, VAEDecode, KSampler, LoadImage, QwenImage21Cache, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, EmptyLatentImage, ComfySwitchNode, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1624, "sampler_name": "euler", "scheduler": "simple", "seed": 980875041290279, "steps": 25, "width": 1080}
---

# 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `980875041290279`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1624`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
