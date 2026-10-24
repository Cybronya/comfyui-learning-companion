---
key: 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json
name: Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json
hash: 3ebbeb0f7fc79090
coverage: 0.8
learned_at: 2026-10-23 11:12:42
nodes: [MarkdownNote, TextEncodeQwenImage21, QwenImage21Cache, ComfySwitchNode, VAEDecode, KSampler, easy imageConcat, VAELoader, JjkText, CLIPLoader, UNETLoader, easy imageConcat, EmptyLatentImage, ImageResizeKJv2, PrimitiveInt, LoadImage, LoadImage, ImageResizeKJv2, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 666374359751542, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 人物替换+图片换人！B站艾橘溪_2109524734416351233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy imageConcat`
- `VAELoader`
- `JjkText`
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy imageConcat`
- `EmptyLatentImage` ★核心
- `ImageResizeKJv2`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `666374359751542`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`easy imageConcat`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`ImageResizeKJv2`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
