---
key: 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json
name: 心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json
hash: 6b0d1bec5c761a4a
coverage: 0.403846
learned_at: 2026-10-20 01:52:31
nodes: [UNETLoader, QwenImage21Cache, CLIPLoader, CLIPLoader, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, EmptyLatentImage, VAEDecode, SetNode, LoadImage, SetNode, LoadImage, SetNode, SetNode, 忽略多组孤海, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BatchImagesNode, SaveImage, GetNode, TextEncodeQwenImage21, GetNode, GetNode, KSampler, CR Prompt Text, TextGenerateLTX2Prompt, ResolutionSelector, SetNode, GetNode, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 420570451358539, "steps": 40, "width": 1024}
---

# 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `忽略多组孤海`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `SaveImage`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Prompt Text`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `SetNode`
- `GetNode`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `420570451358539`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（21/52）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`忽略多组孤海`、`VAELoader`、`BatchImagesNode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`CR Prompt Text`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
