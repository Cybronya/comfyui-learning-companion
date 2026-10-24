---
key: 图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json
name: Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json
hash: 806c73852588480c
coverage: 0.878049
learned_at: 2026-10-23 11:12:48
nodes: [UNETLoader, CLIPLoader, VAELoader, easy seed, KSampler (Efficient), TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1一键透视光影融图产品完美融入背景 产品图融合方案_2109776737675595778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy seed`
- `KSampler (Efficient)` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
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

**识别到的模式**：text_to_image

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

覆盖率 **88%**（36/41）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy seed`、`KSampler (Efficient)`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`KSampler`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
