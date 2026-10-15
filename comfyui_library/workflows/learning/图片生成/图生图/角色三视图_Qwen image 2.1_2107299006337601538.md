---
key: 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json
name: 角色三视图_Qwen image 2.1_2107299006337601538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json
hash: 75d60c1473730dbe
coverage: 1
learned_at: 2026-10-10 21:22:51
nodes: [KSampler, KSampler, VAEDecode, ImageStitch, QwenImage21Cache, VAELoader, UNETLoader, CLIPLoader, VAEDecode, LoadImage, ImageScaleToTotalPixels, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 107308238506398, "steps": 25, "width": 1536}
---

# 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json`

## 结构

**节点**（16 个）：
- `KSampler`
- `KSampler`
- `VAEDecode`
- `ImageStitch`
- `QwenImage21Cache`
- `VAELoader`
- `UNETLoader`
- `CLIPLoader`
- `VAEDecode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `2048`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `107308238506398`
- `steps` = `25`
- `width` = `1536`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`KSampler`、`VAEDecode`、`ImageStitch`、`QwenImage21Cache`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`SaveImageAdvanced`、`SaveImage`
