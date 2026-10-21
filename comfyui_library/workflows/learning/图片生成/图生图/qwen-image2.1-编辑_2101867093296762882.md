---
key: 图片生成/图生图/qwen-image2.1-编辑_2101867093296762882.json
name: qwen-image2.1-编辑_2101867093296762882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1-编辑_2101867093296762882.json
hash: 2ac72a8477730fe7
coverage: 0.730769
learned_at: 2026-10-21 00:46:08
nodes: [ResolutionSelector, MarkdownNote, Note, LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveInt, LoadImage, VAEDecode, SaveImage, TextGenerateLTX2Prompt, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 343569498145940, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image2.1-编辑_2101867093296762882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image2.1-编辑_2101867093296762882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `PreviewAny`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `343569498145940`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
