---
key: 图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json
name: Qwen_Image_2.1_｜生图及编辑_2109445975751352321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json
hash: c56fc22abff43d87
coverage: 0.696429
learned_at: 2026-10-23 11:21:13
nodes: [VAELoader, VAEDecode, EmptyLatentImage, ResolutionSelector, UNETLoader, CLIPLoader, MarkdownNote, Note, SaveImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, Note, MarkdownNote, QwenImage21Cache, ResolutionSelector, MarkdownNote, Note, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, TextEncodeQwenImage21, Note, ComfySwitchNode, LoraLoaderModelOnly, MarkdownNote, LoadImage, LoadImage, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, Note, MarkdownNote, QwenImage21Cache, ResolutionSelector, Note, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, Note, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "bong_tangent", "seed": 277175323402932, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_｜生图及编辑_2109445975751352321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `Note`
- `SaveImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `QwenImage21Cache`
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `Note`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Note`
- `MarkdownNote`
- `QwenImage21Cache`
- `ResolutionSelector`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `Note`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `277175323402932`
- `steps` = `50`
- `cfg` = `3.5`
- `sampler_name` = `er_sde`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **70%**（39/56）

**有卡**：`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`LoadImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
