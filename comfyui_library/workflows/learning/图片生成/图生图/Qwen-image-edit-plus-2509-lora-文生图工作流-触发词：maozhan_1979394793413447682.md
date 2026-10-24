---
key: 图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json
name: Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json
hash: 0e854b85a555a264
coverage: 0.785714
learned_at: 2026-10-23 11:18:09
nodes: [TextEncodeQwenImageEditPlus, CLIPTextEncode, LoraLoader, VAELoader, UNETLoader, CLIPLoader, JjkText, KSampler, EmptyLatentImage, VAEDecode, MarkdownNote, LoadImage, SaveImage, PreviewImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1920, "lora_name": "Qwen-edit-2059-毛毡效果-15.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 833956113019428, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 1080}
---

# 图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Qwen-edit-2059-毛毡效果-15.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `833956113019428`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`LoraLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
