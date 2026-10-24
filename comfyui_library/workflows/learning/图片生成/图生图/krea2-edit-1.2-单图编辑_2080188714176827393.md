---
key: 图片生成/图生图/krea2-edit-1.2-单图编辑_2080188714176827393.json
name: krea2-edit-1.2-单图编辑_2080188714176827393
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2-edit-1.2-单图编辑_2080188714176827393.json
hash: b80885a39a306d87
coverage: 0.933333
learned_at: 2026-10-23 11:40:18
nodes: [KSampler, PreviewImage, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPLoader, Krea2EditGroundedEncode, VAELoader, LoadImage, CR Prompt Text, Krea2EditModelPatch, Krea2EditGroundedEncode, VAEEncode, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 947254408888845, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/krea2-edit-1.2-单图编辑_2080188714176827393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2-edit-1.2-单图编辑_2080188714176827393.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Krea2EditGroundedEncode`
- `VAELoader`
- `LoadImage`
- `CR Prompt Text`
- `Krea2EditModelPatch`
- `Krea2EditGroundedEncode`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `947254408888845`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`KSampler`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`Krea2EditGroundedEncode`、`VAELoader`、`LoadImage`、`CR Prompt Text`、`Krea2EditModelPatch`、`VAEEncode`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
