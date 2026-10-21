---
key: 图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json
name: GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json
hash: ea85c7afd85b7d29
coverage: 0.816667
learned_at: 2026-10-21 02:52:32
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, RH_RhartImageG25SunburstImageToImage, LoadImage, LoadImage, RH_RhartImageG25OfficialTokenSunburstEdit, MuyeTextEditOutput, PlaySound|pysssss, MuyeTextEditOutput, PlaySound|pysssss, PreviewImage, SaveImage, PlaySound|pysssss, RH_RhartImageG25OfficialTokenSunburstTextToImage, MuyeTextEditOutput, LoadImage, LoadImage, PlaySound|pysssss, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, RH_RhartImageG25SunburstTextToImage, MuyeTextEditOutput, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `RH_RhartImageG25SunburstImageToImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG25OfficialTokenSunburstEdit`
- `MuyeTextEditOutput`
- `PlaySound|pysssss`
- `MuyeTextEditOutput`
- `PlaySound|pysssss`
- `PreviewImage`
- `SaveImage`
- `PlaySound|pysssss`
- `RH_RhartImageG25OfficialTokenSunburstTextToImage`
- `MuyeTextEditOutput`
- `LoadImage`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `RH_RhartImageG25SunburstTextToImage`
- `MuyeTextEditOutput`
- `SaveImage`
- `PreviewImage`
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

覆盖率 **82%**（49/60）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG25SunburstImageToImage`、`RH_RhartImageG25OfficialTokenSunburstEdit`、`MuyeTextEditOutput`、`PlaySound|pysssss`、`RH_RhartImageG25OfficialTokenSunburstTextToImage`、`RH_RhartImageG25SunburstTextToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
