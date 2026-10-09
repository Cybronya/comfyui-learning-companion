---
key: 图片生成/图生图/qwen2.1 图生图_2102013171056857089.json
name: qwen2.1 图生图_2102013171056857089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1 图生图_2102013171056857089.json
hash: 9b5fb25e3c3f4de3
coverage: 0.8
learned_at: 2026-10-09 22:27:07
nodes: [VAELoader, CLIPLoader, UNETLoader, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), Int, TextEncodeQwenImage21, KSampler, VAEDecode, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, SaveImage, LoadImage, Text Multiline]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 641504827726597, "steps": 50, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/qwen2.1 图生图_2102013171056857089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102013171056857089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Int`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `641504827726597`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`Int`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
