---
key: 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json
name: qwen2.1基础工作流  i2v  t2v_2102578292409847810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json
hash: af6fa27c2f822fe5
coverage: 0.833333
learned_at: 2026-10-15 22:27:54
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, MarkdownNote, MarkdownNote, Seed (rgthree), UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImageAdvanced, Seed (rgthree), LoadImage, LoadImage, LoadImage, SaveImageAdvanced, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 626015987317164, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `626015987317164`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`Seed (rgthree)`、`QwenImage21Cache`、`SaveImageAdvanced`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
