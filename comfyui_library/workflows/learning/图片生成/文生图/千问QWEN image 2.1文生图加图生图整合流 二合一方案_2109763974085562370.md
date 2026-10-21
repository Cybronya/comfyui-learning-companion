---
key: 图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json
name: 千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json
hash: c0c5a3b1df6f0276
coverage: 0.802817
learned_at: 2026-10-21 02:59:17
nodes: [LoadImage, LoadImage, SaveImage, PreviewImage, VAELoader, CLIPLoader, EmptyLatentImage, PlaySound|pysssss, VAEDecode, TextEncodeQwenImage21, KSampler, JjkText, JjkText, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, UNETLoader, QwenImage21Cache, PlaySound|pysssss, UNETLoader, TextEncodeQwenImage21, VAEDecode, easy int, LoadImage, JjkText, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PreviewImage, SaveImage, Image Comparer (rgthree), easy int, ResolutionSelector, ComfySwitchNode, JjkText, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（71 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `JjkText`
- `JjkText`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `PlaySound|pysssss`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `easy int`
- `LoadImage`
- `JjkText`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy int`
- `ResolutionSelector`
- `ComfySwitchNode`
- `JjkText`
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

覆盖率 **80%**（57/71）

**有卡**：`LoadImage`、`SaveImage`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`PlaySound|pysssss`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`easy int`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
