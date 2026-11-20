---
key: 图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json
name: Qwen2.1-图生图16参考_2115314444816445442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json
hash: 9556666875a79b68
coverage: 1
learned_at: 2026-10-30 17:51:05
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, EmptyLatentImage, KSampler, VAEDecode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 0.7, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1006692058604017, "steps": 50, "width": 1920}
---

# 图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `1006692058604017`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
