---
key: 图片生成/文生图/Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082.json
name: Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082.json
hash: 68f32e954614c3a6
coverage: 0.88
learned_at: 2026-10-19 21:47:03
nodes: [UNETLoader, ImageScaleToTotalPixels, CLIPTextEncode, LoraLoaderModelOnly, PreviewImage, QwenImageDiffsynthControlnet, ConditioningZeroOut, KSampler, KSampler, EmptyLatentImage, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, ImageConcanate, LoadImage, GetImageSize, CLIPLoader, VAELoader, SaveImage, CR Text, AIO_Preprocessor, ModelPatchLoader, Note, Note, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.75, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 765783174981053, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image文生图Controlnet+lora(支持cn和lora)加速版_2003393632608686082.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageConcanate`
- `LoadImage`
- `GetImageSize`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `CR Text`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `Note`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `765783174981053`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`UNETLoader`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`QwenImageDiffsynthControlnet`、`ConditioningZeroOut`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageConcanate`、`LoadImage`、`GetImageSize`、`CLIPLoader`、`VAELoader`、`SaveImage`、`CR Text`、`AIO_Preprocessor`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
