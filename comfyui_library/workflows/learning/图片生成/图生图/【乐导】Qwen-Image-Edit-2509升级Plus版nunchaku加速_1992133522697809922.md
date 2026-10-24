---
key: 图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json
name: 【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json
hash: 119845b59f312ab9
coverage: 0.947368
learned_at: 2026-10-23 11:49:20
nodes: [ModelSamplingAuraFlow, VAEDecode, SaveImage, KSampler, Image Comparer (rgthree), NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEEncode, ConditioningZeroOut, UNETLoader, UnetLoaderGGUF, LoraLoaderModelOnly, ImageScaleToTotalPixels, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 159831616807296, "steps": 20, "width": 512}
---

# 图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `159831616807296`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`KSampler`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEEncode`、`ConditioningZeroOut`、`UNETLoader`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`LoadImage`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
