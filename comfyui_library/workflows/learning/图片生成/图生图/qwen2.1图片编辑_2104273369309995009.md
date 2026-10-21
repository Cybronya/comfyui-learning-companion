---
key: 图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json
name: qwen2.1图片编辑_2104273369309995009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json
hash: 3ecc30c7c1016dd0
coverage: 0.958333
learned_at: 2026-10-21 00:46:11
nodes: [ResolutionSelector, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, UNETLoader, CLIPLoader, TextEncodeQwenImage21, LoadImage, LoadImage, Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1112700527248691, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1112700527248691`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`LoadImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
