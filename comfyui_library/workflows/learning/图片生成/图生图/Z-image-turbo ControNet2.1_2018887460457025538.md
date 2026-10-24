---
key: 图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json
name: Z-image-turbo ControNet2.1_2018887460457025538
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json
hash: e3b46e04efdc108f
coverage: 0.933333
learned_at: 2026-10-23 11:31:01
nodes: [ModelPatchLoader, CLIPTextEncode, ImageScaleToTotalPixels, PreviewImage, VAEEncode, VAELoader, VAEDecode, KSampler, CLIPLoader, AIO_Preprocessor, UNETLoader, LoadImage, QwenImageDiffsynthControlnet, CLIPTextEncode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 273089487860088, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image-turbo ControNet2.1_2018887460457025538.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `VAEEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `LoadImage`
- `QwenImageDiffsynthControlnet`
- `CLIPTextEncode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `273089487860088`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`ModelPatchLoader`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`VAEEncode`、`VAELoader`、`VAEDecode`、`KSampler`、`CLIPLoader`、`AIO_Preprocessor`、`UNETLoader`、`LoadImage`、`QwenImageDiffsynthControlnet`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
