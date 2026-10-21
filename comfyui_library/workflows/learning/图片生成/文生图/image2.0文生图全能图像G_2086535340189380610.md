---
key: 图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json
name: image2.0文生图全能图像G_2086535340189380610
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json
hash: 4c0ecfb07c1875fd
coverage: 0.777778
learned_at: 2026-10-20 00:59:51
nodes: [RH_RhartImageG2TextToImage, SaveImage, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPLoader, solarL_SaveImagesToZip, VAELoader, CLIPTextEncode, CLIPTextEncode, JjkText, VAEDecode, EmptyLatentImage, Note, 孤海注释, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `solarL_SaveImagesToZip`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `孤海注释`
- `孤海注释`

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

覆盖率 **78%**（14/18）

**有卡**：`RH_RhartImageG2TextToImage`、`SaveImage`、`CR Text`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`CLIPLoader`、`solarL_SaveImagesToZip`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
