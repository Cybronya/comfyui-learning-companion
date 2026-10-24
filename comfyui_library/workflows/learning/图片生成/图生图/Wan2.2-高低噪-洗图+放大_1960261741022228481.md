---
key: 图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json
name: Wan2.2-高低噪-洗图+放大_1960261741022228481
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json
hash: 83a00f5f48058871
coverage: 0.862069
learned_at: 2026-10-23 11:28:08
nodes: [LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEEncode, VAELoader, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, SaveImage, KSampler, SaveImage, Bjornulf_TextToStringAndSeed, VAEDecode, PDIMAGE_LongerSize, Anything Everywhere, PMRF, VAEDecode, PathchSageAttentionKJ, Anything Everywhere, LoadImage, Image Comparer (rgthree), PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 497163970725457, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-高低噪-洗图+放大_1960261741022228481.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `Bjornulf_TextToStringAndSeed`
- `VAEDecode` ★核心
- `PDIMAGE_LongerSize`
- `Anything Everywhere`
- `PMRF`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `Anything Everywhere`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`SaveImage`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`PDIMAGE_LongerSize`、`PMRF`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
