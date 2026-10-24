---
key: 图片生成/图生图/qwen_image_edit_plus_use_name_1977395256004091906.json
name: qwen_image_edit_plus_use_name_1977395256004091906
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_use_name_1977395256004091906.json
hash: f0f75755cceb30e4
coverage: 1
learned_at: 2026-10-23 11:44:10
nodes: [VAEDecode, SaveImage, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 751790761855546, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_use_name_1977395256004091906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_use_name_1977395256004091906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `751790761855546`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
