---
key: 图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json
name: Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json
hash: bf1d4e9b0c7b20f6
coverage: 0.714286
learned_at: 2026-10-10 20:48:10
nodes: [MarkdownNote, Note, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, SaveImageAdvanced, ComfySwitchNode, UNETLoader, LoadImage, TextEncodeQwenImage21, SaveImage, EmptyLatentImage, KSampler, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, PrimitiveStringMultiline, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 197012889592863, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1自动分镜_短剧分镜_2102322312635834369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `197012889592863`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImageAdvanced`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
