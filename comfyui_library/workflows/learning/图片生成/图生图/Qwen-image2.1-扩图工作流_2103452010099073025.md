---
key: 图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json
name: Qwen-image2.1-扩图工作流_2103452010099073025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json
hash: 4238879ba5414506
coverage: 0.857143
learned_at: 2026-10-21 00:43:27
nodes: [UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, LoadImage, ImagePadForOutpaint, VAEDecode, SaveImage, PreviewImage, CR Prompt Text, DrawMaskOnImage, PreviewImage, VAELoader, TextEncodeQwenImage21, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 427977582852940, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `LoadImage`
- `ImagePadForOutpaint`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `CR Prompt Text`
- `DrawMaskOnImage`
- `PreviewImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`

## 关键参数

- `seed` = `427977582852940`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`LoadImage`、`ImagePadForOutpaint`、`VAEDecode`、`SaveImage`、`CR Prompt Text`、`DrawMaskOnImage`、`VAELoader`、`TextEncodeQwenImage21`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
