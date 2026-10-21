---
key: 图片生成/图生图/（五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306.json
name: （五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306.json
hash: cf65ae6b32815a2e
coverage: 0.875
learned_at: 2026-10-21 00:57:13
nodes: [UNETLoader, CLIPLoader, VAELoader, SaveImage, QwenImage21Cache, VAEDecode, KSampler, PreviewImage, Image Comparer (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 195683475053953, "steps": 40}
---

# 图片生成/图生图/（五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（五图编辑）Qwen-image-2.1-单图编辑_2104871202018914306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `195683475053953`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
