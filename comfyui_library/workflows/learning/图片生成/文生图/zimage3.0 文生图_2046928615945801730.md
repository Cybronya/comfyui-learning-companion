---
key: 图片生成/文生图/zimage3.0 文生图_2046928615945801730.json
name: zimage3.0 文生图_2046928615945801730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/zimage3.0 文生图_2046928615945801730.json
hash: 45df3eb307eab5b4
coverage: 1
learned_at: 2026-10-21 02:57:52
nodes: [UNETLoader, CLIPLoader, KSampler, EmptyLatentImage, Seed (rgthree), VAELoader, LayerUtility: PurgeVRAM V2, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1044160720030426, "steps": 10, "width": 1080}
---

# 图片生成/文生图/zimage3.0 文生图_2046928615945801730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/zimage3.0 文生图_2046928615945801730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1044160720030426`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`Seed (rgthree)`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、Seed (rgthree)
