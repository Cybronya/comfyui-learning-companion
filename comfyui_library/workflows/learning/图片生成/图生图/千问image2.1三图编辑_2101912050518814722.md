---
key: 图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json
name: 千问image2.1三图编辑_2101912050518814722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json
hash: fce1113d7e04f067
coverage: 0.875
learned_at: 2026-10-21 00:50:39
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, SaveImage, KSampler, QwenImage21Cache, VAEDecode, ComfySwitchNode, MarkdownNote, LoadImage, LoadImage, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1120663159570345, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `SaveImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1120663159570345`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`KSampler`、`QwenImage21Cache`、`VAEDecode`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
