---
key: 图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json
name: Qwen image 2.1 文生图-V1_2101852626458599426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json
hash: 3d768ec10a2cd4f4
coverage: 0.785714
learned_at: 2026-10-20 01:51:06
nodes: [TextEncodeQwenImage21, VAEDecode, CLIPLoader, VAELoader, UNETLoader, SaveImage, PrimitiveStringMultiline, ResolutionSelector, KSampler, CLIPLoader, TextGenerateLTX2Prompt, easy showAnything, EmptyLatentImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 789557471099717, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图-V1_2101852626458599426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `789557471099717`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`TextEncodeQwenImage21`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`、`ResolutionSelector`、`KSampler`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
