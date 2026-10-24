---
key: 图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json
name: FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json
hash: 8615f91a740dc98c
coverage: 0.891304
learned_at: 2026-10-23 10:54:15
nodes: [CR Text, JoinStrings, Image Comparer (rgthree), AILab_ColorInput, VAELoader, KSampler, GetImageSize+, PainterFluxImageEdit, CLIPLoader, VAEDecode, SaveImage, ConstrainImage|pysssss, LoraLoaderModelOnly, UNETLoader, RMBG, ImageLoader, CR Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CR Text`
- `JoinStrings`
- `Image Comparer (rgthree)`
- `AILab_ColorInput`
- `VAELoader`
- `KSampler` ★核心
- `GetImageSize+`
- `PainterFluxImageEdit`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ConstrainImage|pysssss`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `RMBG`
- `ImageLoader`
- `CR Text`
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

覆盖率 **89%**（41/46）

**有卡**：`CR Text`、`JoinStrings`、`AILab_ColorInput`、`VAELoader`、`KSampler`、`GetImageSize+`、`PainterFluxImageEdit`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`ConstrainImage|pysssss`、`LoraLoaderModelOnly`、`UNETLoader`、`RMBG`、`ImageLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
