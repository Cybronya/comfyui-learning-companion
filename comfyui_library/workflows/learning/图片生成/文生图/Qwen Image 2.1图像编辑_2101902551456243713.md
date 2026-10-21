---
key: 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json
name: Qwen Image 2.1图像编辑_2101902551456243713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json
hash: 93464aed513e1af1
coverage: 0.833333
learned_at: 2026-10-20 01:50:55
nodes: [ResolutionSelector, MarkdownNote, Note, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, Note, TextEncodeQwenImage21, SaveImage, easy cleanGpuUsed, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 435198382009480, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `Note`
- `TextEncodeQwenImage21`
- `SaveImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `435198382009480`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`easy cleanGpuUsed`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
