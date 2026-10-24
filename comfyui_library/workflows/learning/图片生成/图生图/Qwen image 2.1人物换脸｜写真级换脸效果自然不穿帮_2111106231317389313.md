---
key: 图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json
name: Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json
hash: 5e81f8188167a0cd
coverage: 0.907692
learned_at: 2026-10-23 11:14:00
nodes: [CLIPLoader, VAELoader, ImageConcanate, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, EmptyLatentImage, Latent Switch (JPS), ImageConcanate, LoadImage, UNETLoader, LoadImage, TextEncodeQwenImage21, CR Text, LoraLoaderModelOnly, KSampler, VAEDecode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1人物换脸｜写真级换脸效果自然不穿帮_2111106231317389313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `CLIPLoader`
- `VAELoader`
- `ImageConcanate`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `Latent Switch (JPS)`
- `ImageConcanate`
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **91%**（59/65）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageConcanate`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`Latent Switch (JPS)`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`CR Text`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
