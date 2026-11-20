---
key: 平台全量/Qwen Image 2.1溶图工作流，图片融合其它图片处理方案_2106870833393262594.json
name: Qwen Image 2.1溶图工作流，图片融合其它图片处理方案_2106870833393262594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1溶图工作流，图片融合其它图片处理方案_2106870833393262594.json
hash: f63b53e6afbef77c
coverage: 0.893617
learned_at: 2026-11-14 00:50:06
nodes: [CLIPLoader, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, KSampler, LoraLoaderModelOnly, VAELoader, UNETLoader, DF_Text_Box, QwenImage21BlockCacheT8, VAEDecode, TextEncodeQwenImage21GH, LoadImage, Image Comparer (rgthree), DetailTransfer, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LayerUtility: ImageRemoveAlpha, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen Image 2.1溶图工作流，图片融合其它图片处理方案_2106870833393262594.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1溶图工作流，图片融合其它图片处理方案_2106870833393262594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21GH`
- `LoadImage`
- `Image Comparer (rgthree)`
- `DetailTransfer`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LayerUtility: ImageRemoveAlpha`
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

覆盖率 **89%**（42/47）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`VAEDecode`、`TextEncodeQwenImage21GH`、`LoadImage`、`DetailTransfer`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageRemoveAlpha`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
