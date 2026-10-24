---
key: 图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json
name: Wan2.2 +lora宠物+文生图_1986964422252015617
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json
hash: b82e61498089eff2
coverage: 0.947368
learned_at: 2026-10-23 11:27:56
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, Anything Everywhere, ModelSamplingSD3, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, LoadImage, VAELoader, CLIPLoader, RH_Captioner, SaveImage, LoraLoaderModelOnly, EmptyLatentImage, VAEDecode, ImageScale]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1504, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 120706270303637, "steps": 8, "width": 1504}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `Anything Everywhere`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `RH_Captioner`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageScale`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `120706270303637`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1504`
- `height` = `1504`
- `batch_size` = `4`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`VAELoader`、`CLIPLoader`、`RH_Captioner`、`SaveImage`、`EmptyLatentImage`、`VAEDecode`、`ImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
