---
key: 图片生成/文生图/Qwen Image 2.1_2102977844501639169.json
name: Qwen Image 2.1_2102977844501639169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1_2102977844501639169.json
hash: f8d2c83becd69444
coverage: 0.9
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, CLIPLoader, KSampler, VAEDecode, SaveImage, CLIPLoader, UNETLoader, VAELoader, QwenImage21Cache, ComfySwitchNode, KSampler, VAEDecode, SaveImage, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, LoadImage, EmptyLatentImage, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "bong_tangent", "seed": 986840392602112, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1_2102977844501639169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1_2102977844501639169.json`

## 结构

**节点**（20 个）：
- `UNETLoader`
- `CLIPLoader`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `LoadImage`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `batch_size` = `1`
- `cfg` = `3.5`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `er_sde`
- `scheduler` = `bong_tangent`
- `seed` = `986840392602112`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`QwenImage21Cache`、`ComfySwitchNode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`
