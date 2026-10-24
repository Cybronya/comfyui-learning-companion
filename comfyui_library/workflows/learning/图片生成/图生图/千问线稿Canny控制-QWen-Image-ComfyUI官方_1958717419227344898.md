---
key: 图片生成/图生图/千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898.json
name: 千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898.json
hash: 647c13940683fa4c
coverage: 0.95
learned_at: 2026-10-23 12:31:42
nodes: [VAELoader, CLIPLoader, UNETLoader, SaveImage, SaveImage, VAEDecode, ImageStitch, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, CLIPTextEncode, ModelPatchLoader, Text Multiline, QwenImageDiffsynthControlnet, EmptySD3LatentImage, GetImageSize, AIO_Preprocessor, LoadImage, ImageScaleDownToSize, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 926796733493595, "steps": 20}
---

# 图片生成/图生图/千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问线稿Canny控制-QWen-Image-ComfyUI官方_1958717419227344898.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageStitch`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`
- `Text Multiline`
- `QwenImageDiffsynthControlnet`
- `EmptySD3LatentImage`
- `GetImageSize`
- `AIO_Preprocessor`
- `LoadImage`
- `ImageScaleDownToSize`
- `PreviewImage`

## 关键参数

- `seed` = `926796733493595`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`VAEDecode`、`ImageStitch`、`ModelSamplingAuraFlow`、`KSampler`、`CLIPTextEncode`、`ModelPatchLoader`、`Text Multiline`、`QwenImageDiffsynthControlnet`、`EmptySD3LatentImage`、`GetImageSize`、`AIO_Preprocessor`、`LoadImage`、`ImageScaleDownToSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet
