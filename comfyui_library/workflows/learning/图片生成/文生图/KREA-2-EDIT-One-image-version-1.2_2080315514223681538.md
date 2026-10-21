---
key: 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json
name: KREA-2-EDIT-One-image-version-1.2_2080315514223681538
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json
hash: 73c55e0b29ce2093
coverage: 0.882353
learned_at: 2026-10-20 00:38:55
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAEEncode, VAEDecode, KSampler, SaveImage, ConditioningZeroOut, EmptySD3LatentImage, Krea2EditModelPatch, GetImageSize, VAELoader, Image Comparer (rgthree), PreviewImage, LoadImage, ResizeImageMaskNode, Krea2EditGroundedEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 594250631586137, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Krea2EditModelPatch`
- `GetImageSize`
- `VAELoader`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `ResizeImageMaskNode`
- `Krea2EditGroundedEncode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `594250631586137`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`Krea2EditModelPatch`、`GetImageSize`、`VAELoader`、`LoadImage`、`ResizeImageMaskNode`、`Krea2EditGroundedEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
