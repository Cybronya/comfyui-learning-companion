---
key: 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562.json
name: 【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562.json
hash: 1dbc8bbfaf84061d
coverage: 0.952381
learned_at: 2026-11-14 01:26:09
nodes: [ModelSamplingAuraFlow, VAEDecode, SaveImage, KSampler, Image Comparer (rgthree), NunchakuQwenImageDiTLoader, LoadImage, CLIPLoader, VAELoader, LoadImage, EmptyLatentImage, TextEncodeQwenImageEditPlus_lrzjason, VAEEncode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, UNETLoader, UnetLoaderGGUF, LoraLoaderModelOnly, ImageScaleToTotalPixels, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 863137901475239, "steps": 20, "width": 512}
---

# 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `NunchakuQwenImageDiTLoader`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `863137901475239`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`KSampler`、`NunchakuQwenImageDiTLoader`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus_lrzjason`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`UNETLoader`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
