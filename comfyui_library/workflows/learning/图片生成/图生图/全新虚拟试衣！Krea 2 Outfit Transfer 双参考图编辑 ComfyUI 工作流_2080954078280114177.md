---
key: 图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json
name: 全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json
hash: da2c15872638c44f
coverage: 0.863636
learned_at: 2026-10-23 12:13:15
nodes: [Krea2EditGroundedEncode, Note, PreviewImage, GetImageSize, VAEEncode, EmptySD3LatentImage, VAEDecode, KSampler, Krea2EditModelPatch, SaveImage, ImageScaleBy, UNETLoader, LoraLoaderModelOnly, CLIPLoader, ResizeImageMaskNode, VAELoader, ResizeImageMaskNode, VAEEncode, PreviewImage, LoadImage, LoadImage, Krea2EditGroundedEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 615272749946642, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `Krea2EditGroundedEncode`
- `Note`
- `PreviewImage`
- `GetImageSize`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Krea2EditModelPatch`
- `SaveImage`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ResizeImageMaskNode`
- `VAELoader`
- `ResizeImageMaskNode`
- `VAEEncode` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `Krea2EditGroundedEncode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `615272749946642`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`Krea2EditGroundedEncode`、`GetImageSize`、`VAEEncode`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`Krea2EditModelPatch`、`SaveImage`、`ImageScaleBy`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ResizeImageMaskNode`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
