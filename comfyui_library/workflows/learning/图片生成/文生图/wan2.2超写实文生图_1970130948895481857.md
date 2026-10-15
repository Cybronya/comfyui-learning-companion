---
key: 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json
name: wan2.2超写实文生图_1970130948895481857
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json
hash: 60cea33b7befb1ca
coverage: 1
learned_at: 2026-10-15 22:27:59
nodes: [LayerUtility: PurgeVRAM, EmptyLatentImage, LoraLoaderModelOnly, PathchSageAttentionKJ, CheckpointLoaderSimple, CLIPTextEncode, KSampler, VAEDecode, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 1, "height": 1280, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 739786914323188, "steps": 10, "width": 1280}
---

# 图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2超写实文生图_1970130948895481857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `LayerUtility: PurgeVRAM`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `1280`
- `batch_size` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`
- `seed` = `739786914323188`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`LayerUtility: PurgeVRAM`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、PathchSageAttentionKJ
