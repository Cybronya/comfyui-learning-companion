---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json
name: Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json
hash: 38391819fe97e571
coverage: 0.916667
learned_at: 2026-10-23 11:16:25
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), RHHiddenNodes, QwenImage21Cache, LoadImage, TextInput_, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 944243028727670, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `RHHiddenNodes`
- `QwenImage21Cache`
- `LoadImage`
- `TextInput_`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `944243028727670`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`、`RHHiddenNodes`、`QwenImage21Cache`、`LoadImage`、`TextInput_`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
