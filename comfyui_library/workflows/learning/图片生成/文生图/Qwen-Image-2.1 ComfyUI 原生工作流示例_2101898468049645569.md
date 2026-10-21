---
key: 图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json
name: Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json
hash: 8db70df8c0629d82
coverage: 0.818182
learned_at: 2026-10-20 01:51:14
nodes: [VAELoader, EmptyLatentImage, MarkdownNote, MarkdownNote, VAEDecode, SaveImage, ResolutionSelector, KSampler, CLIPLoader, TextEncodeQwenImage21, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 172749325695422, "steps": 35, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `172749325695422`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`KSampler`、`CLIPLoader`、`TextEncodeQwenImage21`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
