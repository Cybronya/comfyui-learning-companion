---
key: 图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json
name: BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json
hash: 5b1908bf752452b7
coverage: 0.92
learned_at: 2026-10-10 21:26:22
nodes: [VAELoader, VAEDecode, QwenImage21Cache, KSampler, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, UNETLoader, SaveImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json`

## 结构

**节点**（25 个）：
- `VAELoader`
- `VAEDecode`
- `QwenImage21Cache`
- `KSampler`
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage`
- `UNETLoader`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `999`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`KSampler`、`ComfySwitchNode`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`LoadImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`SaveImageAdvanced`

**缺卡**（1）：`CR Prompt Text`

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
