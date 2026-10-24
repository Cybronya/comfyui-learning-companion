---
key: 图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json
name: qwen_image_edit_plus_MultipleAngles_1986272902184128514
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json
hash: e8141a8644b349a3
coverage: 1
learned_at: 2026-10-23 11:44:06
nodes: [CLIPTextEncode, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, LoraLoaderModelOnly, SaveImage, LoadImage, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 29505298411573, "steps": 8, "width": 1440}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_MultipleAngles_1986272902184128514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `29505298411573`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
