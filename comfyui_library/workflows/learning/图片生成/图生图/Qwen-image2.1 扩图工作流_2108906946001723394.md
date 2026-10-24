---
key: 图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json
name: Qwen-image2.1 扩图工作流_2108906946001723394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json
hash: 60514967b29e4c6f
coverage: 0.928571
learned_at: 2026-10-23 11:18:20
nodes: [DrawMaskOnImage, CLIPLoader, VAELoader, UNETLoader, LoadImage, PreviewImage, LoraLoaderModelOnly, CR Prompt Text, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, KSampler, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 87417016386474, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `DrawMaskOnImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `KSampler` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `87417016386474`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`DrawMaskOnImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`CR Prompt Text`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`KSampler`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
