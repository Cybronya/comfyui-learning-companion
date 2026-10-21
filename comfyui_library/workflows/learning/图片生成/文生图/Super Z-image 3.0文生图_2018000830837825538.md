---
key: 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json
name: Super Z-image 3.0文生图_2018000830837825538
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json
hash: 4d6f704cba0a210e
coverage: 0.785714
learned_at: 2026-10-19 22:15:19
nodes: [CLIPTextEncode, KSampler, VAELoader, PrimitiveNode, LayerUtility: PurgeVRAM, VAEDecode, SaveImage, CLIPLoader, CLIPTextEncode, PrimitiveInt, PrimitiveInt, EmptyLatentImage, CR Prompt Text, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 876956632014829, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `876956632014829`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`EmptyLatentImage`、`CR Prompt Text`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
