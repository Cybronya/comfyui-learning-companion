---
key: sd1.5/basic.json
name: basic
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/sd1.5/basic.json
hash: a95cceecfb5d5225
coverage: 1
learned_at: 2026-10-06 03:49:53
nodes: [CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "sd15_base_model.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 261660645921551, "steps": 20, "width": 512}
---

# sd1.5/basic.json

> 来源文件 `comfyui_library/workflows/sd1.5/basic.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（7 个）：
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sd15_base_model.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `261660645921551`
- `steps` = `20`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
