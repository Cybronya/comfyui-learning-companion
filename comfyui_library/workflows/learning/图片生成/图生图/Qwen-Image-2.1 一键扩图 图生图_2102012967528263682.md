---
key: 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json
name: Qwen-Image-2.1 一键扩图 图生图_2102012967528263682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json
hash: 6534ee17a8d0f516
coverage: 0.875
learned_at: 2026-10-21 00:43:11
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, SaveImage, JjkText, LoadImage, KSampler, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 652115060241845, "steps": 45, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`
- `JjkText`
- `LoadImage`
- `KSampler` ★核心
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `652115060241845`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
