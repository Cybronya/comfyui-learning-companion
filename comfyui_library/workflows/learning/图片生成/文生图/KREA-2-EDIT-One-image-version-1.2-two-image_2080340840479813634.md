---
key: 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json
name: KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json
hash: 2c825dd1e4b0627f
coverage: 0.952381
learned_at: 2026-10-20 00:38:55
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAEDecode, KSampler, ConditioningZeroOut, Image Comparer (rgthree), VAEEncode, EmptySD3LatentImage, SaveImage, ResizeImageMaskNode, ResizeImageMaskNode, GetImageSize, VAEEncode, Krea2EditModelPatch, ResizeImageMaskNode, VAELoader, Krea2EditGroundedEncode, LoadImage, LoadImage, Krea2EditGroundedEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 84715307399109, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `VAEEncode` ★核心
- `Krea2EditModelPatch`
- `ResizeImageMaskNode`
- `VAELoader`
- `Krea2EditGroundedEncode`
- `LoadImage`
- `LoadImage`
- `Krea2EditGroundedEncode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `84715307399109`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`VAEEncode`、`EmptySD3LatentImage`、`SaveImage`、`ResizeImageMaskNode`、`GetImageSize`、`Krea2EditModelPatch`、`VAELoader`、`Krea2EditGroundedEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
