---
key: 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json
name: Y_qwen_image_2.1_t2i_2108495280059535362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json
hash: 2dec120d1e728a7a
coverage: 0.733333
learned_at: 2026-10-20 01:51:32
nodes: [MarkdownNote, MarkdownNote, UNETLoader, TextEncodeQwenImage21, CLIPLoader, KSampler, QwenImage21Cache, VAELoader, VAEDecode, EmptyLatentImage, ResolutionSelector, PrimitiveStringMultiline, MarkdownNote, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 45, "width": 1024}
---

# 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`KSampler`、`QwenImage21Cache`、`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
