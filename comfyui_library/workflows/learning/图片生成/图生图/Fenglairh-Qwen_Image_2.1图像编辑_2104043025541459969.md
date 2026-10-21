---
key: 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json
name: Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json
hash: 7f629490e1b97ced
coverage: 0.5625
learned_at: 2026-10-21 00:39:17
nodes: [UNETLoader, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, GetNode, LoadImage, LoadImage, MarkdownNote, Note, QwenImage21Cache, KSampler, GetNode, VAEDecode, easy cleanGpuUsed, SetNode, TextEncodeQwenImage21, PrimitiveStringMultiline, GetNode, SaveImage, ResolutionSelector, EmptyLatentImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 150703489256539, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
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
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `150703489256539`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（18/32）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
