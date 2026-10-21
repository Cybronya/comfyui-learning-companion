---
key: 图片生成/图生图/换装+换衣_Outfit_Changes_Clothing_Changes_FireRed_2102958212864630786.json
name: 换装+换衣_Outfit_Changes_Clothing_Changes_FireRed_2102958212864630786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换装+换衣_Outfit_Changes_Clothing_Changes_FireRed_2102958212864630786.json
hash: d64888b0ee156d3d
coverage: 0.866667
learned_at: 2026-10-21 00:53:49
nodes: [CLIPLoader, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, SaveImage, PreviewImage, PIP_图像联结, VAELoader, VAEDecode, ConditioningZeroOut, LoadImage, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 240884129316651, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/换装+换衣_Outfit_Changes_Clothing_Changes_FireRed_2102958212864630786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换装+换衣_Outfit_Changes_Clothing_Changes_FireRed_2102958212864630786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `PIP_图像联结`
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `240884129316651`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`SaveImage`、`PIP_图像联结`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`LoadImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
