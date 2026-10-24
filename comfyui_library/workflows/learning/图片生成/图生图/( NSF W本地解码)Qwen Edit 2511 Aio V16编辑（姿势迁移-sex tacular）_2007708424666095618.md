---
key: 图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json
name: ( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json
hash: f1939e9ebd0543ca
coverage: 1
learned_at: 2026-10-23 10:46:30
nodes: [GetImageSizeAndCount, CLIPLoader, VAELoader, SaveImage, VAEDecode, LoraLoaderModelOnly, Text Multiline, LoadImage, ImageScaleToTotalPixels, DuckHideNode, SaveImage, TT_img_enc, TT_img_enc_v2, SaveImage, CR Prompt Text, CheckpointLoaderSimple, DWPreprocessor, LoadImage, KSampler, TextEncodeQwenImageEditPlus, EmptyLatentImage, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, SaveImage, ImageConcanate, ImageConcanate, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v16.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "beta57", "seed": 757634177514880, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `GetImageSizeAndCount`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `DuckHideNode`
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `SaveImage`
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `DWPreprocessor`
- `LoadImage`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v16.safetensors`
- `seed` = `757634177514880`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `768`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`GetImageSizeAndCount`、`CLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`LoraLoaderModelOnly`、`Text Multiline`、`LoadImage`、`ImageScaleToTotalPixels`、`DuckHideNode`、`TT_img_enc`、`TT_img_enc_v2`、`CR Prompt Text`、`CheckpointLoaderSimple`、`DWPreprocessor`、`KSampler`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
