---
key: 图片生成/文生图/地表最强全能图片G2文生图｜GP-T-Image-2单次0.1元｜性价比拉满_2104049104883118081.json
name: 地表最强全能图片G2文生图｜GP-T-Image-2单次0.1元｜性价比拉满_2104049104883118081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/地表最强全能图片G2文生图｜GP-T-Image-2单次0.1元｜性价比拉满_2104049104883118081.json
hash: 2e487be806a1fb09
coverage: 0.9375
learned_at: 2026-10-10 20:59:41
nodes: [Text, Float, RTXVideoSuperResolution, RH_RhartImageG2TextToImage, SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/地表最强全能图片G2文生图｜GP-T-Image-2单次0.1元｜性价比拉满_2104049104883118081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/地表最强全能图片G2文生图｜GP-T-Image-2单次0.1元｜性价比拉满_2104049104883118081.json`

## 结构

**节点**（48 个）：
- `Text`
- `Float`
- `RTXVideoSuperResolution`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **94%**（45/48）

**有卡**：`Text`、`Float`、`RTXVideoSuperResolution`、`RH_RhartImageG2TextToImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
