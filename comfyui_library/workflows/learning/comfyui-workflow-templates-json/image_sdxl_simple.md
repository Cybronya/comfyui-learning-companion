---
key: comfyui-workflow-templates-json/image_sdxl_simple.json
name: image_sdxl_simple
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_sdxl_simple.json
hash: f13ce5e57ecd3b7c
official: true
coverage: 0.875
learned_at: 2026-10-10 22:48:39
nodes: [SaveImage, CLIPTextEncode, CLIPTextEncode, KSampler, EmptyLatentImage, VAEDecode, CheckpointLoaderSimple, MarkdownNote]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "sd_xl_base_1.0.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 812045847300606, "steps": 25, "width": 1024}
---

# comfyui-workflow-templates-json/image_sdxl_simple.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_sdxl_simple.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（8 个）：
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `812045847300606`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sd_xl_base_1.0.safetensors`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`SaveImage`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
