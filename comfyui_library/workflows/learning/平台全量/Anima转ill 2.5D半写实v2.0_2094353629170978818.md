---
key: 平台全量/Anima转ill 2.5D半写实v2.0_2094353629170978818.json
name: Anima转ill 2.5D半写实v2.0_2094353629170978818
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Anima转ill 2.5D半写实v2.0_2094353629170978818.json
hash: 42daf4c4b8b52a8a
coverage: 0.909091
learned_at: 2026-11-14 00:19:16
nodes: [CLIPLoader, VAELoader, VAEDecode, ClownsharKSampler_Beta, VAEDecode, ImageUpscaleWithModel, EmptyLatentImage, PreviewImage, UNETLoader, SaveImage, CLIPTextEncode, CheckpointLoaderSimple, LoraLoader, LoraLoaderModelOnly, UpscaleModelLoader, CLIPTextEncode, LatentUpscaleBy, VAEEncode, KSampler, PreviewImage, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "miaomiaoRealskin_epsV13.safetensors", "denoise": 0.25000000000000006, "height": 1152, "lora_name": "shiej007.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 9396810451531, "steps": 30, "strength_clip": 1, "strength_model": 0.10000000000000002, "width": 896}
---

# 平台全量/Anima转ill 2.5D半写实v2.0_2094353629170978818.json

> 来源文件 `comfyui_library/workflows/平台全量/Anima转ill 2.5D半写实v2.0_2094353629170978818.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `9396810451531`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.25000000000000006`
- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`
- `checkpoint` = `miaomiaoRealskin_epsV13.safetensors`
- `lora_name` = `shiej007.safetensors`
- `strength_model` = `0.10000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`ClownsharKSampler_Beta`、`ImageUpscaleWithModel`、`EmptyLatentImage`、`UNETLoader`、`SaveImage`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoader`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`LatentUpscaleBy`、`VAEEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode
