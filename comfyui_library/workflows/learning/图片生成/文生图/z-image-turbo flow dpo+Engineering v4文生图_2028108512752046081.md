---
key: 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json
name: z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json
hash: 41d3500c338c7197
coverage: 1
learned_at: 2026-10-19 22:46:15
nodes: [ConditioningZeroOut, VAELoader, CLIPTextEncode, VAEDecode, CLIPLoaderGGUF, LoraLoaderModelOnly, KSampler, LoadImage, UNETLoader, easy seed, SaveImage, CR Prompt Text, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 369009184023090, "steps": 10, "width": 1080}
---

# 图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image-turbo flow dpo+Engineering v4文生图_2028108512752046081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `easy seed`
- `SaveImage`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `369009184023090`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoaderGGUF`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`UNETLoader`、`easy seed`、`SaveImage`、`CR Prompt Text`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
