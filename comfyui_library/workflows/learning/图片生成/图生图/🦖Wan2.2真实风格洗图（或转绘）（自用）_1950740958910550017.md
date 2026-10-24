---
key: 图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json
name: 🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json
hash: 70645042a0d8bbe4
coverage: 1
learned_at: 2026-10-23 13:40:52
nodes: [UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, KSampler, PMRF, VAEDecode, Bjornulf_TextToStringAndSeed, VAEEncode, VAELoader, PDIMAGE_LongerSize, SaveImage, VAEDecode, LoadImage, KSampler, CLIPLoader, ModelSamplingSD3, SaveImage, PDIMAGE_LongerSize, ImageConcanate, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 497163970725457, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PMRF`
- `VAEDecode` ★核心
- `Bjornulf_TextToStringAndSeed`
- `VAEEncode` ★核心
- `VAELoader`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`PMRF`、`VAEDecode`、`Bjornulf_TextToStringAndSeed`、`VAEEncode`、`VAELoader`、`PDIMAGE_LongerSize`、`SaveImage`、`LoadImage`、`CLIPLoader`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
