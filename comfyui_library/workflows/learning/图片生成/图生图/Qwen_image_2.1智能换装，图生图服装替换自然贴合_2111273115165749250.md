---
key: 图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json
name: Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json
hash: b012eb8a3c03f2a8
coverage: 0.901961
learned_at: 2026-10-23 11:21:30
nodes: [CLIPLoader, VAELoader, ImageConcanate, VAEDecode, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, LoadImage, EmptyLatentImage, Latent Switch (JPS), ImageConcanate, UNETLoader, LoraLoaderModelOnly, KSampler, TextEncodeQwenImage21, CR Text, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1智能换装，图生图服装替换自然贴合_2111273115165749250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `CLIPLoader`
- `VAELoader`
- `ImageConcanate`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Latent Switch (JPS)`
- `ImageConcanate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CR Text`
- `LoadImage`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **90%**（46/51）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`Latent Switch (JPS)`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`TextEncodeQwenImage21`、`CR Text`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
