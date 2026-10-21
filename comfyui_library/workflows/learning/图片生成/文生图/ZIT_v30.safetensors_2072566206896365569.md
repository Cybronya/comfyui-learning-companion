---
key: 图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json
name: ZIT_v30.safetensors_2072566206896365569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json
hash: 135962eb4a5a4dce
coverage: 1
learned_at: 2026-10-19 23:42:11
nodes: [CLIPLoaderGGUF, VAELoader, EmptyLatentImage, easy int, CLIPTextEncode, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage, LoraLoaderModelOnly, easy int, easy int, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 905887863698976, "steps": 10, "width": 512}
---

# 图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoaderGGUF`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `easy int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `905887863698976`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoaderGGUF`、`VAELoader`、`EmptyLatentImage`、`easy int`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、UNETLoader、CLIPLoaderGGUF
