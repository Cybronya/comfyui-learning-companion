---
key: sd1.5/text-to-image-workflow.png
name: text-to-image-workflow
type: Text To Image
status: completed
source: png
file: comfyui_library/workflows/sd1.5/text-to-image-workflow.png
hash: d154255b8120e645
coverage: 1
learned_at: 2026-10-10 00:07:05
nodes: [EmptyLatentImage, KSampler, VAEDecode, SaveImage, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "v1-5-pruned-emaonly-fp16.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 156680208700286, "steps": 20, "width": 512}
---

# sd1.5/text-to-image-workflow.png

> 来源文件 `comfyui_library/workflows/sd1.5/text-to-image-workflow.png`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（7 个）：
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `156680208700286`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `v1-5-pruned-emaonly-fp16.safetensors`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
