---
key: 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json
name: Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json
hash: b98d30a2f4c282a1
coverage: 0.842105
learned_at: 2026-10-21 00:44:02
nodes: [KSampler, VAEDecode, KSampler, VAEDecode, QwenImage21Cache, VAELoader, EmptyLatentImage, ImageScaleToTotalPixels, CLIPLoader, EmptyLatentImage, ImageStitch, SaveImage, ComfySwitchNode, LoadImage, UNETLoader, TextEncodeQwenImage21, JjkText, TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 993075727452513, "steps": 25, "width": 1536}
---

# 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
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
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `JjkText`
- `TextEncodeQwenImage21`
- `JjkText`

## 关键参数

- `seed` = `993075727452513`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ImageStitch`、`SaveImage`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
