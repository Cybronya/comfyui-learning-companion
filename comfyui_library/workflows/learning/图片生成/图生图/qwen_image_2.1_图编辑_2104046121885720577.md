---
key: 图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json
name: qwen_image_2.1_图编辑_2104046121885720577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json
hash: b489cfc9c1a02365
coverage: 0.823529
learned_at: 2026-10-21 00:46:21
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, VAEDecode, SaveImage, KSampler, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 178005621473640, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `178005621473640`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`SaveImage`、`KSampler`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
