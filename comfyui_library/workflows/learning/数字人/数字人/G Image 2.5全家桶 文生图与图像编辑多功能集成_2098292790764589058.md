---
key: 数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json
name: G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json
hash: 8b83d9d9b6346d5c
coverage: 0.74
learned_at: 2026-10-19 00:19:08
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree), PreviewImage, RH_RhartImageG25OfficialTokenFlareEdit, PreviewImage, SaveImage, RH_RhartImageG25OfficialTokenFlareTextToImage, Fast Groups Bypasser (rgthree), SaveImage, JjkText, SaveImage, RH_RhartImageG25SunburstImageToImage, RH_RhartImageG25SunburstTextToImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `RH_RhartImageG25OfficialTokenFlareEdit`
- `PreviewImage`
- `SaveImage`
- `RH_RhartImageG25OfficialTokenFlareTextToImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `JjkText`
- `SaveImage`
- `RH_RhartImageG25SunburstImageToImage`
- `RH_RhartImageG25SunburstTextToImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
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
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
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

覆盖率 **74%**（37/50）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG25OfficialTokenFlareEdit`、`RH_RhartImageG25OfficialTokenFlareTextToImage`、`RH_RhartImageG25SunburstImageToImage`、`RH_RhartImageG25SunburstTextToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
