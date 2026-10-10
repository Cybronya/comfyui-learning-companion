---
key: 图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json
name: Qwen-image2.1-人像多角度生成_2101942834889838593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json
hash: 22bc3dd1961c1fba
coverage: 0.764706
learned_at: 2026-10-10 20:48:09
nodes: [CLIPLoader, VAELoader, UNETLoader, KSampler, TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, easy promptList, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, easy showAnything, VAEDecode, SaveImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy promptList]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 273132510218467, "steps": 25}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人像多角度生成_2101942834889838593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `easy promptList`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `easy showAnything`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `273132510218467`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`QwenMultiangleCameraNode`、`VAEDecode`、`SaveImage`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
