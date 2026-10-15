---
key: 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json
name: Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json
hash: ea08dc0da3d5bd43
coverage: 0.548387
learned_at: 2026-10-15 22:25:06
nodes: [UNETLoader, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, GetNode, LoadImage, LoadImage, MarkdownNote, Note, Note, QwenImage21Cache, KSampler, GetNode, VAEDecode, easy cleanGpuUsed, SetNode, TextEncodeQwenImage21, PrimitiveStringMultiline, GetNode, SaveImage, ResolutionSelector, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 351855746137687, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json`

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

覆盖率 **55%**（17/31）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
