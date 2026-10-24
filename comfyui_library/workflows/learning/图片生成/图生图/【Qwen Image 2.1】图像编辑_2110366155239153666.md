---
key: 图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json
name: 【Qwen Image 2.1】图像编辑_2110366155239153666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json
hash: 3d4b4ad3839cfd95
coverage: 0.714286
learned_at: 2026-10-23 11:48:50
nodes: [UNETLoader, VAELoader, SetNode, SetNode, CLIPLoader, CLIPLoader, LoadImage, QwenImage21Cache, CLIPLoader, Anything Everywhere3, TextEncodeQwenImage21, ShowText|pysssss, KSampler, VAEDecode, TextGenerateLTX2Prompt, GetNode, CR Prompt Text, EmptyLatentImage, Note, SaveImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 822404074317978, "steps": 40, "width": 992}
---

# 图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `LoadImage`
- `QwenImage21Cache`
- `CLIPLoader`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `GetNode`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心
- `Note`
- `SaveImage`
- `ResolutionSelector`

## 关键参数

- `seed` = `822404074317978`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `992`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoadImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`EmptyLatentImage`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
