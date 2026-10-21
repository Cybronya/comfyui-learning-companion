---
key: 图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json
name: Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json
hash: a0a50e966b470957
coverage: 0.73913
learned_at: 2026-10-19 22:30:05
nodes: [ConditioningZeroOut, KSampler, CLIPTextEncode, VAELoader, CLIPLoader, easy seed, KSampler, UNETLoader, VAEDecode, AddLabel, AddLabel, EmptyLatentImage, PreviewImage, PreviewImage, PreviewImage, VAEDecode, Note, Note, PreviewImage, CR Prompt Text, ImageConcanate, LoraLoaderModelOnly, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 360498039717611, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `easy seed`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `PreviewImage`
- `CR Prompt Text`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `360498039717611`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`ConditioningZeroOut`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`easy seed`、`UNETLoader`、`VAEDecode`、`AddLabel`、`EmptyLatentImage`、`CR Prompt Text`、`ImageConcanate`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
