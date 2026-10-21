---
key: 图片生成/文生图/ComfyUI system workflow_2072886879170686978.json
name: ComfyUI system workflow_2072886879170686978
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI system workflow_2072886879170686978.json
hash: 036dfde5ce354748
coverage: 0.875
learned_at: 2026-10-20 00:01:06
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, EmptyLatentImage, KSampler, SaveImage, PreviewImage, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "v1-5-pruned-emaonly-fp16.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 926505439476440, "steps": 20, "width": 512}
---

# 图片生成/文生图/ComfyUI system workflow_2072886879170686978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI system workflow_2072886879170686978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `926505439476440`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `v1-5-pruned-emaonly-fp16.safetensors`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
