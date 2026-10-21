---
key: 图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json
name: 图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json
hash: 51efa72a02db6d90
coverage: 0.85
learned_at: 2026-10-21 02:59:36
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, JjkText, LoadImage, PrimitiveInt, QwenImage21Cache, ImageResizeKJv2, ImageResizeKJv2, EmptyLatentImage, TextEncodeQwenImage21, easy imageConcat, ComfySwitchNode, ImageScale, KSampler, VAEDecode, SaveImage, easy imageConcat, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta", "seed": 666374359751542, "steps": 25, "width": 960}
---

# 图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `JjkText`
- `LoadImage`
- `PrimitiveInt`
- `QwenImage21Cache`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `easy imageConcat`
- `ComfySwitchNode`
- `ImageScale`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageConcat`
- `SaveImage`

## 关键参数

- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `666374359751542`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`ImageResizeKJv2`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`easy imageConcat`、`ImageScale`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
