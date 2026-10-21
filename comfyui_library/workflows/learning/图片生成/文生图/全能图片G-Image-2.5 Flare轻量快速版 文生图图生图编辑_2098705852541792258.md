---
key: 图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json
name: 全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json
hash: fa5643e3e04fef9c
coverage: 0.846154
learned_at: 2026-10-20 01:35:20
nodes: [SaveImage, PreviewImage, SaveImage, PreviewImage, RH_RhartImageG25OfficialTokenFlareEdit, LoadImage, LoadImage, LoadImage, LoadImage, RH_RhartImageG25OfficialTokenSunburstTextToImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `RH_RhartImageG25OfficialTokenFlareEdit`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG25OfficialTokenSunburstTextToImage`
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

覆盖率 **85%**（33/39）

**有卡**：`SaveImage`、`RH_RhartImageG25OfficialTokenFlareEdit`、`LoadImage`、`RH_RhartImageG25OfficialTokenSunburstTextToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
