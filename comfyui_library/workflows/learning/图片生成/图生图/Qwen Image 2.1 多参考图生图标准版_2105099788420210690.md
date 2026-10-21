---
key: 图片生成/图生图/Qwen Image 2.1 多参考图生图标准版_2105099788420210690.json
name: Qwen Image 2.1 多参考图生图标准版_2105099788420210690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多参考图生图标准版_2105099788420210690.json
hash: 8d19df4c575d3b55
coverage: 0.869565
learned_at: 2026-10-21 00:42:13
nodes: [CLIPLoader, VAELoader, MarkdownNote, MarkdownNote, EmptyLatentImage, UNETLoader, ComfySwitchNode, ResolutionSelector, QwenImage21Cache, TextEncodeQwenImage21, KSampler, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42995774240821, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 多参考图生图标准版_2105099788420210690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多参考图生图标准版_2105099788420210690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42995774240821`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`ResolutionSelector`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
