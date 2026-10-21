---
key: 图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json
name: Qwen2.1图像编辑_2101937813171302401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json
hash: ae280bf4731c0c2f
coverage: 1
learned_at: 2026-10-21 00:43:38
nodes: [CLIPLoader, UNETLoader, LoadImage, LoadImage, LoadImage, EmptyLatentImage, VAELoader, VAEDecode, Seed (rgthree), ResolutionSelector, SaveImage, KSampler, TextEncodeQwenImage21, StringToInt, LoadImage, LoadImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1051260549848279, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `ResolutionSelector`
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `StringToInt`
- `LoadImage`
- `LoadImage`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1051260549848279`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`UNETLoader`、`LoadImage`、`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`Seed (rgthree)`、`ResolutionSelector`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`StringToInt`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
