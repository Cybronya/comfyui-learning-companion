---
key: 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json
name: qwen+image+2.1多图编辑_2102637659226206209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json
hash: e17aefa7f6a0c44b
coverage: 0.85
learned_at: 2026-10-10 20:59:24
nodes: [CLIPLoader, KSampler, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, VAELoader, UNETLoader, VAEDecode, SaveImage, LoadImage, LoadImage, LoadImage, TextGenerateLTX2Prompt, CLIPLoader, BatchImagesNode, CR Text, LoadImage, TextEncodeQwenImage21, easy showAnything]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1121348690810382, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json`

## 结构

**节点**（20 个）：
- `CLIPLoader`
- `KSampler`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `ResolutionSelector`
- `VAELoader`
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `BatchImagesNode`
- `CR Text`
- `LoadImage`
- `TextEncodeQwenImage21`
- `easy showAnything`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1121348690810382`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`KSampler`、`QwenImage21Cache`、`ComfySwitchNode`、`EmptyLatentImage`、`ResolutionSelector`、`VAELoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`CR Text`

**缺卡**（1）：`CR Text`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
