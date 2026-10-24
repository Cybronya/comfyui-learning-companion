---
key: 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json
name: qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json
hash: 221e18f32d5dd01f
coverage: 0.869565
learned_at: 2026-10-23 11:43:03
nodes: [VAELoader, CLIPLoader, KSamplerAdvanced, TextEncodeQwenImage21, CR Prompt Text, VAEDecode, Image Comparer (rgthree), LoadImage, INTConstant, SimpleMath+, PreviewImage, InpaintCropImproved, VAEEncode, SetLatentNoiseMask, UNETLoader, InpaintStitchImproved, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `INTConstant`
- `SimpleMath+`
- `PreviewImage`
- `InpaintCropImproved`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `UNETLoader` ★核心
- `InpaintStitchImproved`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`TextEncodeQwenImage21`、`CR Prompt Text`、`VAEDecode`、`LoadImage`、`INTConstant`、`SimpleMath+`、`InpaintCropImproved`、`VAEEncode`、`SetLatentNoiseMask`、`UNETLoader`、`InpaintStitchImproved`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
