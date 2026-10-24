---
key: 图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json
name: 文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json
hash: d2bc87a60768eb1f
coverage: 0.958333
learned_at: 2026-10-23 13:03:43
nodes: [ConditioningZeroOut, VAEDecode, QwenImageDiffsynthControlnet, KSampler, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, ModelPatchLoader, ImageUpscaleWithModel, SaveImage, ImageConcanate, UNETLoader, AIO_Preprocessor, ImageScaleToTotalPixels, LoraLoaderModelOnly, CLIPTextEncode, CR Text, GetImageSize, LoadImage, LoadImage, PreviewImage, UpscaleModelLoader, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.75, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 128277742123911, "steps": 10, "width": 1024}
---

# 图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/文生图Zimage文生图动作迁移Controlnet+lora(支持cn和lora)加速版_1996857207276851202.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ModelPatchLoader`
- `ImageUpscaleWithModel`
- `SaveImage`
- `ImageConcanate`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `GetImageSize`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `UpscaleModelLoader`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `128277742123911`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`QwenImageDiffsynthControlnet`、`KSampler`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ModelPatchLoader`、`ImageUpscaleWithModel`、`SaveImage`、`ImageConcanate`、`UNETLoader`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CR Text`、`GetImageSize`、`LoadImage`、`UpscaleModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
