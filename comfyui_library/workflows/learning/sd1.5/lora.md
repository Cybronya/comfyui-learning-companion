---
key: sd1.5/lora.png
name: lora
type: Text To Image
status: completed
source: png
file: comfyui_library/workflows/sd1.5/lora.png
hash: 9d318e7ac04c1fdf
coverage: 0.888889
learned_at: 2026-10-07 22:22:23
nodes: [VAEDecode, SaveImage, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, LoraLoader, CheckpointLoaderSimple, KSampler, MarkdownNote]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "dreamshaper_8.safetensors", "denoise": 1, "height": 768, "lora_name": "blindbox_v1_mix.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 261660645921551, "steps": 30, "strength_clip": 1, "strength_model": 0.75, "width": 768}
---

# sd1.5/lora.png

> 来源文件 `comfyui_library/workflows/sd1.5/lora.png`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `MarkdownNote`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `lora_name` = `blindbox_v1_mix.safetensors`
- `strength_model` = `0.75`
- `strength_clip` = `1`
- `checkpoint` = `dreamshaper_8.safetensors`
- `seed` = `261660645921551`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoader`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoraLoader、LoraLoader、SaveImage
