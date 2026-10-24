---
key: 图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073.json
name: Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073.json
hash: 33bdf5c462784406
coverage: 0.961538
learned_at: 2026-10-23 11:07:34
nodes: [VAEEncode, CLIPLoader, VAELoader, ResolutionSelector, VAELoader, LoraLoaderModelOnly, UNETLoader, TextInput_, Krea2EditGroundedEncode, Krea2EditGroundedEncode, EmptySD3LatentImage, VAEDecode, SaveImage, SaveImage, Krea2EditModelPatch, Float, Note, ResizeImageMaskNode, KSampler, SaveImage, SaveImage, LoadImage, SaveImage, SaveImage, ImageConcanate, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 109700506684254, "steps": 10}
---

# 图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextInput_`
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `Krea2EditModelPatch`
- `Float`
- `Note`
- `ResizeImageMaskNode`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `109700506684254`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`VAEEncode`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`LoraLoaderModelOnly`、`UNETLoader`、`TextInput_`、`Krea2EditGroundedEncode`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`Krea2EditModelPatch`、`Float`、`ResizeImageMaskNode`、`KSampler`、`LoadImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
