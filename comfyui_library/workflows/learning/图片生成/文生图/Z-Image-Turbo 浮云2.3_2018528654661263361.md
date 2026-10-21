---
key: 图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json
name: Z-Image-Turbo 浮云2.3_2018528654661263361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json
hash: c0f812dc1ea808e2
coverage: 0.769231
learned_at: 2026-10-19 22:29:59
nodes: [KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, PrimitiveInt, CLIPLoader, UNETLoader, PrimitiveInt, PrimitiveNode, VAELoader, VAEDecode, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 215525430068639, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveNode`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `215525430068639`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
