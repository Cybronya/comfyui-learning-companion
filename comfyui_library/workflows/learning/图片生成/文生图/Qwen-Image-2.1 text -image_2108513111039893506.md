---
key: 图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json
name: Qwen-Image-2.1 text -image_2108513111039893506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json
hash: 796614a6df4fc806
coverage: 1
learned_at: 2026-10-20 01:51:15
nodes: [KSampler, CR Text, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextEncodeQwenImage21, QwenImage21Cache, ResolutionSelector, VAEDecode, SaveImage, CompressImages]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `CompressImages`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`KSampler`、`CR Text`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`CompressImages`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
