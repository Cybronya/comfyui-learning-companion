---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json
name: LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json
hash: 1fa02153e5090bd5
coverage: 0.933333
learned_at: 2026-10-23 11:08:39
nodes: [UNETLoader, CLIPLoader, VAELoader, ImpactInt, CR Text, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, PrimitiveNode, VAEEncode, ConditioningZeroOut, VAEDecode, KSampler, SaveImage, LoadImage, Qwen3_VQA]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 780471543212639, "steps": 10}
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `Qwen3_VQA`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `780471543212639`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`VAEEncode`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
