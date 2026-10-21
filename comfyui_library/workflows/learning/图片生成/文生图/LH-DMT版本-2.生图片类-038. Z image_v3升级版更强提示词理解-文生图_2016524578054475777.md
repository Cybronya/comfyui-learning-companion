---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json
name: LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json
hash: 8f85b8215a37c9c7
coverage: 1
learned_at: 2026-10-19 22:15:13
nodes: [UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, LayerUtility: PurgeVRAM, VAEDecode, SaveImage, CLIPTextEncode, KSampler, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 873211290661696, "steps": 20, "width": 1080}
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `873211290661696`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
