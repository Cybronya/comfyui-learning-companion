---
key: 图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json
name: GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json
hash: ad3609f7ae846b7f
coverage: 0.797297
learned_at: 2026-10-07 03:05:05
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, RH_RhartImageG25SunburstImageToImage, LoadImage, LoadImage, RH_RhartImageG25OfficialTokenSunburstEdit, MuyeTextEditOutput, PlaySound|pysssss, MuyeTextEditOutput, PlaySound|pysssss, PreviewImage, SaveImage, PlaySound|pysssss, RH_RhartImageG25OfficialTokenSunburstTextToImage, MuyeTextEditOutput, LoadImage, LoadImage, PlaySound|pysssss, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, RH_RhartImageG25SunburstTextToImage, MuyeTextEditOutput, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
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

覆盖率 **80%**（59/74）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG25SunburstImageToImage`、`RH_RhartImageG25OfficialTokenSunburstEdit`、`MuyeTextEditOutput`、`RH_RhartImageG25OfficialTokenSunburstTextToImage`、`RH_RhartImageG25SunburstTextToImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（4）：`PlaySound|pysssss`、`PlaySound|pysssss`、`PlaySound|pysssss`、`PlaySound|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
