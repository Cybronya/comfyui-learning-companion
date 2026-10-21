---
key: 图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json
name: Qwen Image 2.1 标准文生图工作流_2101851852332687361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json
hash: bea9712c88318ed7
coverage: 0.666667
learned_at: 2026-10-20 01:50:53
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, MarkdownNote, 孤海注释, 孤海注释, EmptyLatentImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2000, "sampler_name": "euler", "scheduler": "simple", "seed": 861496183617560, "steps": 25, "width": 1600}
---

# 图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `孤海注释`
- `孤海注释`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `861496183617560`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1600`
- `height` = `2000`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（8/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
