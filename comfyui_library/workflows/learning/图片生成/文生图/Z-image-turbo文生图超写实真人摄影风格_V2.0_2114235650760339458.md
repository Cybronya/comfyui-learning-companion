---
key: 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json
name: Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json
hash: 2ed72de97852a5a2
coverage: 1
learned_at: 2026-10-26 22:08:57
nodes: [ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEDecode, LoraLoaderModelOnly, KSampler, UNETLoader, CLIPTextEncode, EmptyLatentImage, SaveImage, LoraLoaderModelOnly, CR Latent Input Switch, EmptyLatentImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1042466983535146, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CR Latent Input Switch`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1042466983535146`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`CR Latent Input Switch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
