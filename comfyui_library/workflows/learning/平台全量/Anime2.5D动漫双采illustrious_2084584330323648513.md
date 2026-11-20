---
key: 平台全量/Anime2.5D动漫双采illustrious_2084584330323648513.json
name: Anime2.5D动漫双采illustrious_2084584330323648513
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Anime2.5D动漫双采illustrious_2084584330323648513.json
hash: bf10d7c1b006bda6
coverage: 0.588235
learned_at: 2026-11-14 00:19:20
nodes: [Note, CLIPTextEncode, KSampler, VAEDecode, PreviewImage, LatentUpscaleBy, KSampler, VAEDecode, SaveImage, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, Note, EmptyLatentImage, CheckpointLoaderSimple, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "checkpoint": "Snow2.5D.safetensors", "denoise": 0.45000000000000007, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 1052171578192150, "steps": 20, "width": 768}
---

# 平台全量/Anime2.5D动漫双采illustrious_2084584330323648513.json

> 来源文件 `comfyui_library/workflows/平台全量/Anime2.5D动漫双采illustrious_2084584330323648513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `Note`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LatentUpscaleBy`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1052171578192150`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.45000000000000007`
- `width` = `768`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `Snow2.5D.safetensors`

## 知识

覆盖率 **59%**（10/17）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEDecode`、`LatentUpscaleBy`、`SaveImage`、`EmptyLatentImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LatentUpscaleBy、SaveImage、image_to_image_controlnet_face_detailer_lora
