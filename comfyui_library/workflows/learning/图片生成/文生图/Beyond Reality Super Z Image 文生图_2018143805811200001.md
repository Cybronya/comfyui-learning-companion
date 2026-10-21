---
key: 图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json
name: Beyond Reality Super Z Image 文生图_2018143805811200001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json
hash: df896e85aeb6beb3
coverage: 1
learned_at: 2026-10-19 22:14:55
nodes: [CLIPTextEncode, CLIPTextEncode, KSampler, VAELoader, VAEDecode, SaveImage, Int, Int, Int, Int, Int, Int, Int, CLIPLoader, Int, Int, Int, Int, Int, LoraLoaderModelOnly, easy int, EmptyLatentImage, UNETLoader, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, easy int, easy int, Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 428220940048559, "steps": 10, "width": 1152}
---

# 图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `CLIPLoader`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `easy int`
- `easy int`
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `428220940048559`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（42/42）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`Int`、`CLIPLoader`、`LoraLoaderModelOnly`、`easy int`、`EmptyLatentImage`、`UNETLoader`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
