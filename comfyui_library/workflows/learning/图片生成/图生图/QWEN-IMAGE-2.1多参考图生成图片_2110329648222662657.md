---
key: 图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json
name: QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json
hash: 85e584286c9b4f46
coverage: 0.923077
learned_at: 2026-10-23 11:11:14
nodes: [SaveImage, VAEDecode, KSampler, LoadImage, QwenImage21Cache, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, ComfySwitchNode, UNETLoader, EmptySD3LatentImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 951977699767560, "steps": 25}
---

# 图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

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
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `951977699767560`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`UNETLoader`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
