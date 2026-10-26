---
key: 图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json
name: 图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json
hash: c76779d9f97defd5
coverage: 0.818182
learned_at: 2026-10-26 22:05:42
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, JjkText, LoadImage, PrimitiveInt, QwenImage21Cache, ImageResizeKJv2, ImageResizeKJv2, EmptyLatentImage, TextEncodeQwenImage21, easy imageConcat, ComfySwitchNode, ImageScale, KSampler, VAEDecode, SaveImage, easy imageConcat, SaveImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta", "seed": 666374359751542, "steps": 25, "width": 960}
---

# 图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片换人丨Qwen_Image_2.1丨双图替换·保留姿态_2113801696882282497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **82%**（18/22）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`ImageResizeKJv2`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`easy imageConcat`、`ImageScale`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
