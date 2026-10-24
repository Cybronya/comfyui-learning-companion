---
key: 图片生成/图生图/双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041.json
name: 双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041.json
hash: 0a52daaf9fa10091
coverage: 0.84
learned_at: 2026-10-23 12:34:53
nodes: [ResolutionSelector, LoadImage, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, JjkText, LoadImage, LoadImage, JjkText, EmptyLatentImage, QwenImage21Cache, BatchImagesNode, easy imageConcat, TextGenerate, easy imageConcat, ComfySwitchNode, ImageScale, TextEncodeQwenImage21, ComfySwitchNode, KSampler, VAEDecode, SaveImage, easy imageConcat, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 40511518867650, "steps": 50, "width": 1088}
---

# 图片生成/图生图/双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `JjkText`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `BatchImagesNode`
- `easy imageConcat`
- `TextGenerate`
- `easy imageConcat`
- `ComfySwitchNode`
- `ImageScale`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageConcat`
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `40511518867650`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`BatchImagesNode`、`easy imageConcat`、`TextGenerate`、`ImageScale`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
