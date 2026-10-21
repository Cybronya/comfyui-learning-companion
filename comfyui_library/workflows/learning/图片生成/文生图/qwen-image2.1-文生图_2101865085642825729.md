---
key: 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json
name: qwen-image2.1-文生图_2101865085642825729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json
hash: 3e9252c10fdfebd9
coverage: 0.733333
learned_at: 2026-10-20 01:51:58
nodes: [ResolutionSelector, MarkdownNote, Note, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, VAEDecode, KSampler, SaveImage, EmptyLatentImage, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PreviewAny`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`VAEDecode`、`KSampler`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
