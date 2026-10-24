---
key: 图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json
name: Z-image 自动洗图 · 图生图 1.0_1994238581453553666
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json
hash: 52c4ee8b08d6f529
coverage: 0.809524
learned_at: 2026-10-23 11:30:31
nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, SetNode, Qwen3_VQA, ShowText|pysssss, ConditioningZeroOut, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, SaveImage, SaveImage, VAEDecode, GetNode, ImageConcanate, KSampler, PrimitiveFloat, VAEEncode, RHHiddenNodes, RHHiddenNodes]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 637417312958292, "steps": 60}
---

# 图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `ConditioningZeroOut`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `GetNode`
- `ImageConcanate`
- `KSampler` ★核心
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `637417312958292`
- `steps` = `60`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`Qwen3_VQA`、`ConditioningZeroOut`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`KSampler`、`VAEEncode`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
