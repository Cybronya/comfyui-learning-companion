---
key: 图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json
name: 千问image2.1双图编辑_2101908220829851649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json
hash: c48da5ccb102c933
coverage: 0.866667
learned_at: 2026-10-21 00:50:39
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, LoadImage, ResolutionSelector, LoadImage, CR Text, SaveImage, KSampler, QwenImage21Cache, VAEDecode, ComfySwitchNode, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 370141094286835, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `CR Text`
- `SaveImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `370141094286835`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`CR Text`、`SaveImage`、`KSampler`、`QwenImage21Cache`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
