---
key: 图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json
name: Qwen2.1_BF16_文生图官方工作流_2101860361765998594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json
hash: 0567878c6cfcf1ff
coverage: 0.588235
learned_at: 2026-10-20 01:51:22
nodes: [MarkdownNote, EmptyLatentImage, 孤海注释, ResolutionSelector, KSampler, 孤海注释, UNETLoader, MarkdownNote, CLIPLoader, Reroute, VAELoader, VAEDecode, Reroute, TextEncodeQwenImage21, JjkText, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 555508346116461, "steps": 45, "width": 1024}
---

# 图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `孤海注释`
- `ResolutionSelector`
- `KSampler` ★核心
- `孤海注释`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `Reroute`
- `VAELoader`
- `VAEDecode` ★核心
- `Reroute`
- `TextEncodeQwenImage21`
- `JjkText`
- `SaveImage`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `555508346116461`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（10/17）

**有卡**：`EmptyLatentImage`、`ResolutionSelector`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
