---
key: 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json
name: Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json
hash: eb22becc57345f92
coverage: 0.769231
learned_at: 2026-10-19 22:29:54
nodes: [CLIPTextEncode, VAELoader, PrimitiveNode, VAEDecode, CLIPLoader, CLIPTextEncode, EmptyLatentImage, UNETLoader, PrimitiveInt, SaveImage, CR Prompt Text, PrimitiveInt, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 767501463572256, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `SaveImage`
- `CR Prompt Text`
- `PrimitiveInt`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `767501463572256`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
