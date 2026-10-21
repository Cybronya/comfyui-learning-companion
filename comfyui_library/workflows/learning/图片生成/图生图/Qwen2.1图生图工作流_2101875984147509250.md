---
key: 图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json
name: Qwen2.1图生图工作流_2101875984147509250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json
hash: e78fae2287728281
coverage: 0.642857
learned_at: 2026-10-21 00:43:39
nodes: [MarkdownNote, CLIPLoader, QwenImage21Cache, VAEDecode, VAELoader, Reroute, GH_ImageVideoComparer, SaveImage, TextEncodeQwenImage21, LoadImage, easy int, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, 孤海注释, MmuuaiGroupBypass, 孤海注释, MarkdownNote, KSampler, UNETLoader, 孤海注释, 孤海注释, 孤海注释, LoadImage, LoadImage, SaveImageAdvanced, LoadImage, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 167798795367023, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `MarkdownNote`
- `CLIPLoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `VAELoader`
- `Reroute`
- `GH_ImageVideoComparer`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `easy int`
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `孤海注释`
- `MmuuaiGroupBypass`
- `孤海注释`
- `MarkdownNote`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `LoadImage`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `167798795367023`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（18/28）

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`VAEDecode`、`VAELoader`、`GH_ImageVideoComparer`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`、`easy int`、`ResolutionSelector`、`EmptyLatentImage`、`MmuuaiGroupBypass`、`KSampler`、`UNETLoader`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
