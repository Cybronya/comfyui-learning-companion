---
key: 图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json
name: Qwen-image2.1-扩图2.0_2104395498009489409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json
hash: 7510c6a10b5e270f
coverage: 0.857143
learned_at: 2026-10-21 00:43:26
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SaveImage, CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, PreviewImage, LoraLoaderModelOnly, CR Prompt Text, ImagePadForOutpaint, LoadImage, KSampler, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 333620156437642, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `ImagePadForOutpaint`
- `LoadImage`
- `KSampler` ★核心
- `PreviewImage`

## 关键参数

- `seed` = `333620156437642`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CR Prompt Text`、`ImagePadForOutpaint`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
