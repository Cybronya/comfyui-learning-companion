---
key: 图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json
name: Qwen image 2.1图片编辑+角色定妆照_2103068698557902850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json
hash: 4351450432cf5abc
coverage: 0.947368
learned_at: 2026-10-21 00:42:57
nodes: [KSampler, VAEDecode, TextEncodeQwenImage21, KSampler, VAEDecode, QwenImage21Cache, VAELoader, EmptyLatentImage, ImageScaleToTotalPixels, CLIPLoader, EmptyLatentImage, ImageStitch, SaveImage, ComfySwitchNode, LoadImage, Label (rgthree), Label (rgthree), TextEncodeQwenImage21, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 206301193234, "steps": 25, "width": 1536}
---

# 图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ImageStitch`
- `SaveImage`
- `ComfySwitchNode`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `206301193234`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ImageStitch`、`SaveImage`、`LoadImage`、`Label (rgthree)`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
