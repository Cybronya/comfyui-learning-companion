---
key: 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json
name: 角色三视图_Qwen image 2.1_2107299006337601538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json
hash: 75d60c1473730dbe
coverage: 0.8125
learned_at: 2026-10-06 21:44:28
nodes: [KSampler, KSampler, VAEDecode, ImageStitch, QwenImage21Cache, VAELoader, UNETLoader, CLIPLoader, VAEDecode, LoadImage, ImageScaleToTotalPixels, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage]
patterns: []
missing: [ImageScaleToTotalPixels, ImageStitch, SaveImageAdvanced]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 107308238506398, "steps": 25, "width": 1536}
discoveries: [次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageStitch` 知识库中没有该节点类型的任何知识, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `QwenImage21Cache`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `seed` = `107308238506398`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21Cache`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`SaveImage`

**缺卡**（3）：`ImageScaleToTotalPixels`、`ImageStitch`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageStitch` 知识库中没有该节点类型的任何知识
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
