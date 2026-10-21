---
key: 图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json
name: （贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json
hash: 982c0d9894d88c38
coverage: 1
learned_at: 2026-10-21 03:03:36
nodes: [ConditioningZeroOut, CLIPTextEncode, VAELoader, CLIPLoader, easy seed, KSampler, UNETLoader, VAEDecode, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, EmptyLatentImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 129801250019880, "steps": 10, "width": 1080}
---

# 图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞lora）z-image-turbo D-OPSD版文生图V1_2056616951438471170.json`

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
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `EmptyLatentImage` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `129801250019880`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`easy seed`、`KSampler`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`SaveImage`、`CR Prompt Text`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
