---
key: 图片生成/图生图/qwen_image_edit_plus_nextscene_1977038049123147778.json
name: qwen_image_edit_plus_nextscene_1977038049123147778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_nextscene_1977038049123147778.json
hash: c88c95183e49e517
coverage: 1
learned_at: 2026-10-23 11:44:08
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, LoraLoaderModelOnly, LoadImage, KSampler, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 44547868198846, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_nextscene_1977038049123147778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_nextscene_1977038049123147778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `44547868198846`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`KSampler`、`UNETLoader`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
