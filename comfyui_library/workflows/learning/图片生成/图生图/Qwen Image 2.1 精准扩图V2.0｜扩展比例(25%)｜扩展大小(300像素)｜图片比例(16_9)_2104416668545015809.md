---
key: 图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json
name: Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json
hash: 9adb20e6f07d3173
coverage: 0.782609
learned_at: 2026-10-21 00:42:15
nodes: [LoadImage, 孤海外补画板按方向, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, KSampler, TextEncodeQwenImage21, Int, Int, Int, Int, PrimitiveNode, PrimitiveNode, SaveImage, VAEDecode, PreviewImage, Int, 孤海注释, 孤海注释, Switch any [Crystools]]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 840934512665482, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LoadImage`
- `孤海外补画板按方向`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `Int`
- `Int`
- `Int`
- `Int`
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `Int`
- `孤海注释`
- `孤海注释`
- `Switch any [Crystools]`

## 关键参数

- `seed` = `840934512665482`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`LoadImage`、`孤海外补画板按方向`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`TextEncodeQwenImage21`、`Int`、`SaveImage`、`VAEDecode`、`Switch any [Crystools]`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
