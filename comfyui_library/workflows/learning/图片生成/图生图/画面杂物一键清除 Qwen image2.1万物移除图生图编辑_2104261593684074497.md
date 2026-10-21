---
key: 图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json
name: 画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json
hash: fd3daeffdfd217c7
coverage: 0.866667
learned_at: 2026-10-21 00:55:25
nodes: [UNETLoader, VAEDecode, SaveImage, PreviewImage, Mask Fill Holes, DrawMaskOnImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, PreviewImage, CR Prompt Text, KSampler, CR Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/画面杂物一键清除 Qwen image2.1万物移除图生图编辑_2104261593684074497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `Mask Fill Holes`
- `DrawMaskOnImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `CR Prompt Text`
- `KSampler` ★核心
- `CR Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **87%**（39/45）

**有卡**：`UNETLoader`、`VAEDecode`、`SaveImage`、`Mask Fill Holes`、`DrawMaskOnImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`KSampler`、`CR Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
