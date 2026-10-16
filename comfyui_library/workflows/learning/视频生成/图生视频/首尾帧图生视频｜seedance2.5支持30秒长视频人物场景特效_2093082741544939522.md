---
key: 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json
name: 首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json
hash: 8b24e3792f731497
coverage: 0.882353
learned_at: 2026-10-16 23:00:16
nodes: [LoadImage, RH_BytedanceSeedance25TokenImageToVideo, SaveVideo, CR Text, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `LoadImage`
- `RH_BytedanceSeedance25TokenImageToVideo`
- `SaveVideo`
- `CR Text`
- `LoadImage`
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

覆盖率 **88%**（30/34）

**有卡**：`LoadImage`、`RH_BytedanceSeedance25TokenImageToVideo`、`SaveVideo`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
