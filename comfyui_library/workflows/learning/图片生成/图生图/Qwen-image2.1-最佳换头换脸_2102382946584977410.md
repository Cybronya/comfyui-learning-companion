---
key: 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json
name: Qwen-image2.1-最佳换头换脸_2102382946584977410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json
hash: 7690cd765035560f
coverage: 0.923077
learned_at: 2026-10-15 22:25:24
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PreviewImage, VAELoader, KSampler, CLIPLoader, UNETLoader, TextEncodeQwenImage21, SaveImage, LoadImage, LoadImage, LoraLoaderModelOnly, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1068832392954113, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-最佳换头换脸_2102382946584977410.json`

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

覆盖率 **92%**（12/13）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VAELoader`、`KSampler`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
