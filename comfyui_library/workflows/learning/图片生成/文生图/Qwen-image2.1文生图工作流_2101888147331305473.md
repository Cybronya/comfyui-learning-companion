---
key: 图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json
name: Qwen-image2.1文生图工作流_2101888147331305473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json
hash: b62e5295ffb209be
coverage: 0.5
learned_at: 2026-10-20 01:51:21
nodes: [孤海注释, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, VAEDecode, SaveImage, EmptyLatentImage, TextGenerateLTX2Prompt, PreviewAny, TextEncodeQwenImage21, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, KSampler, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 866110070152994, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `866110070152994`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **50%**（11/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
