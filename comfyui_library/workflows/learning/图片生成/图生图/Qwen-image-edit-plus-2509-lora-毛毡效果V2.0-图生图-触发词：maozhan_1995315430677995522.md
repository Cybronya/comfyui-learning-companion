---
key: 图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json
name: Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json
hash: 87a38e40d62294a2
coverage: 0.8125
learned_at: 2026-10-23 11:18:10
nodes: [UNETLoader, CLIPLoader, JjkText, MarkdownNote, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, TextEncodeQwenImageEditPlus, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, VAEDecode, AddLabel, SaveImage, LoadImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1920, "lora_name": "Qwen-edit-2509-毛毡效果v2.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 116046898116248, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 1080}
---

# 图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `MarkdownNote`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `AddLabel`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Qwen-edit-2509-毛毡效果v2.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `116046898116248`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`AddLabel`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
