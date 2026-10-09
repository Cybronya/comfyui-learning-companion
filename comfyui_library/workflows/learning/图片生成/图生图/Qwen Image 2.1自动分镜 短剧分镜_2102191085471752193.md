---
key: 图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json
name: Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json
hash: a89236a22380f73e
coverage: 0.736842
learned_at: 2026-10-09 22:27:09
nodes: [MarkdownNote, Note, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, SaveImageAdvanced, ComfySwitchNode, UNETLoader, LoadImage, TextEncodeQwenImage21, SaveImage, EmptyLatentImage, KSampler, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 871110009689816, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102191085471752193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `871110009689816`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImageAdvanced`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
