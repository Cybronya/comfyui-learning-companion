---
key: 图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json
name: Z-image-turbo Vs flow-dpo对比_2026971124013207554
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json
hash: 973098af48cbfa19
coverage: 0.894737
learned_at: 2026-10-19 22:30:05
nodes: [ConditioningZeroOut, KSampler, CLIPTextEncode, VAELoader, CLIPLoader, easy seed, LoraLoaderModelOnly, KSampler, UNETLoader, EmptyLatentImage, CR Prompt Text, PreviewImage, PreviewImage, VAEDecode, VAEDecode, ImageConcanate, AddLabel, AddLabel, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 667094715999690, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `AddLabel`
- `AddLabel`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `667094715999690`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`ConditioningZeroOut`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`easy seed`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyLatentImage`、`CR Prompt Text`、`VAEDecode`、`ImageConcanate`、`AddLabel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
