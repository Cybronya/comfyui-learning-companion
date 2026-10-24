---
key: 图片生成/图生图/qwen_image_edit_plus_unblur_2010375997945815041.json
name: qwen_image_edit_plus_unblur_2010375997945815041
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_unblur_2010375997945815041.json
hash: 68359e23555d54f6
coverage: 0.923077
learned_at: 2026-10-23 11:44:08
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, Note, KSampler, TextEncodeQwenImageEditPlus, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 610083456857582, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_unblur_2010375997945815041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_unblur_2010375997945815041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `610083456857582`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`KSampler`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
