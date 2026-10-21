---
key: 图片生成/图生图/老孙AI_  Qwen Image 2.1图像编辑_2102008010162921474.json
name: 老孙AI_  Qwen Image 2.1图像编辑_2102008010162921474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老孙AI_  Qwen Image 2.1图像编辑_2102008010162921474.json
hash: 78a1b8d5c9e8f4bb
coverage: 0.857143
learned_at: 2026-10-21 00:55:46
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, KSampler, Reroute, EmptyLatentImage, easy ifElse, LoadImage, LoadImage, 图像缩放V2_孤海, LoadImage, UNETLoader, TextEncodeQwenImage21, DF_Text_Box, 布尔孤海, GoohaiUniversalSlider, GH_ImageVideoComparer, SaveImage, ResolutionSelector, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
---

# 图片生成/图生图/老孙AI_  Qwen Image 2.1图像编辑_2102008010162921474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老孙AI_  Qwen Image 2.1图像编辑_2102008010162921474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Reroute`
- `EmptyLatentImage` ★核心
- `easy ifElse`
- `LoadImage`
- `LoadImage`
- `图像缩放V2_孤海`
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `DF_Text_Box`
- `布尔孤海`
- `GoohaiUniversalSlider`
- `GH_ImageVideoComparer`
- `SaveImage`
- `ResolutionSelector`
- `孤海注释`

## 关键参数

- `seed` = `0`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`图像缩放V2_孤海`、`UNETLoader`、`TextEncodeQwenImage21`、`DF_Text_Box`、`布尔孤海`、`GoohaiUniversalSlider`、`GH_ImageVideoComparer`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
