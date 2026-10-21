---
key: 图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json
name: （贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json
hash: 029480c548496f88
coverage: 1
learned_at: 2026-10-19 22:30:43
nodes: [ConditioningZeroOut, CLIPTextEncode, VAELoader, CLIPLoader, easy seed, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, VAEDecode, SaveImage, CR Prompt Text, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 160715738195194, "steps": 10, "width": 1920}
---

# 图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `easy seed`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `160715738195194`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`easy seed`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
