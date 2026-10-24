---
key: 图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202.json
name: Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202.json
hash: 4cff19f4c25093b1
coverage: 0.933333
learned_at: 2026-10-23 11:07:35
nodes: [CLIPLoader, VAELoader, ResolutionSelector, VAELoader, UNETLoader, Krea2EditGroundedEncode, Krea2EditGroundedEncode, EmptySD3LatentImage, Krea2EditModelPatch, ImageConcanate, SaveImage, VAEEncode, VAEEncode, ResizeImageMaskNode, TextInput_, LoadImage, SaveImage, LoraLoaderModelOnly, ResizeImageMaskNode, SaveImage, VAEDecode, Note, LoadImage, Float, Note, Float, KSampler, SaveImage, LoraLoaderModelOnly, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 109700506684254, "steps": 10}
---

# 图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `VAELoader`
- `UNETLoader` ★核心
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `EmptySD3LatentImage`
- `Krea2EditModelPatch`
- `ImageConcanate`
- `SaveImage`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ResizeImageMaskNode`
- `TextInput_`
- `LoadImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `LoadImage`
- `Float`
- `Note`
- `Float`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **93%**（28/30）

**有卡**：`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`UNETLoader`、`Krea2EditGroundedEncode`、`EmptySD3LatentImage`、`Krea2EditModelPatch`、`ImageConcanate`、`SaveImage`、`VAEEncode`、`ResizeImageMaskNode`、`TextInput_`、`LoadImage`、`LoraLoaderModelOnly`、`VAEDecode`、`Float`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
