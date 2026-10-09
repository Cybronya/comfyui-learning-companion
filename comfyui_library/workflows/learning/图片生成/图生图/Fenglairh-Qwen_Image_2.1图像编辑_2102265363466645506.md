---
key: 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json
name: Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json
hash: ea08dc0da3d5bd43
coverage: 0.516129
learned_at: 2026-10-09 22:27:10
nodes: [UNETLoader, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, GetNode, LoadImage, LoadImage, MarkdownNote, Note, Note, QwenImage21Cache, KSampler, GetNode, VAEDecode, easy cleanGpuUsed, SetNode, TextEncodeQwenImage21, PrimitiveStringMultiline, GetNode, SaveImage, ResolutionSelector, EmptyLatentImage]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 351855746137687, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102265363466645506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `Note`
- `Note`
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `GetNode`
- `SaveImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `351855746137687`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（16/31）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
