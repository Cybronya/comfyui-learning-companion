---
key: 图片生成/图生图/qwen_image_2.1智能抠图，图生图主体分离利器_2111287595195002882.json
name: qwen_image_2.1智能抠图，图生图主体分离利器_2111287595195002882
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1智能抠图，图生图主体分离利器_2111287595195002882.json
hash: ae13ac8d86e87995
coverage: 0.844444
learned_at: 2026-10-23 11:43:54
nodes: [JjkText, LoraLoaderModelOnly, QwenImage21Cache, JjkText, CR Text Replace, LoadImage, KSamplerSelect, SamplerCustom, VAEDecode, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, ManualSigmas, VAELoader, CLIPLoader, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_2.1智能抠图，图生图主体分离利器_2111287595195002882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1智能抠图，图生图主体分离利器_2111287595195002882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `JjkText`
- `CR Text Replace`
- `LoadImage`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `ManualSigmas`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
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

覆盖率 **84%**（38/45）

**有卡**：`LoraLoaderModelOnly`、`QwenImage21Cache`、`CR Text Replace`、`LoadImage`、`KSamplerSelect`、`SamplerCustom`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`ManualSigmas`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
