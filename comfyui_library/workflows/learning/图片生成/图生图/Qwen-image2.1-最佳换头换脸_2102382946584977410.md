---
key: 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json
name: Qwen-image2.1-最佳换头换脸_2102382946584977410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json
hash: 7690cd765035560f
coverage: 0.769231
learned_at: 2026-10-09 22:19:27
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PreviewImage, VAELoader, KSampler, CLIPLoader, UNETLoader, TextEncodeQwenImage21, SaveImage, LoadImage, LoadImage, LoraLoaderModelOnly, CR Prompt Text]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1068832392954113, "steps": 25}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102382946584977410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAELoader`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `1068832392954113`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`VAEDecode`、`VAELoader`、`KSampler`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
