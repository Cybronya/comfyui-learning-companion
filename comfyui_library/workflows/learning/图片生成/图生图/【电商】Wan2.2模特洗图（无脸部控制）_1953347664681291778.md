---
key: 图片生成/图生图/【电商】Wan2.2模特洗图（无脸部控制）_1953347664681291778.json
name: 【电商】Wan2.2模特洗图（无脸部控制）_1953347664681291778
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【电商】Wan2.2模特洗图（无脸部控制）_1953347664681291778.json
hash: 17b6832526ab0e71
coverage: 0.966667
learned_at: 2026-10-23 11:50:59
nodes: [LoraLoaderModelOnly, KSampler, KSampler, LayerUtility: ImageReel, LoadImage, LayerUtility: ImageReelComposit, ShowText, CLIPTextEncode, CLIPTextEncode, VAEEncode, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, PDIMAGE_LongerSize, Bjornulf_TextToStringAndSeed, VAEDecode, VAEDecode, SaveImage, SaveImage, PreviewImage, CR Text Concatenate, RHHiddenNodes]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 1039048886568320, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【电商】Wan2.2模特洗图（无脸部控制）_1953347664681291778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【电商】Wan2.2模特洗图（无脸部控制）_1953347664681291778.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `LoadImage`
- `LayerUtility: ImageReelComposit`
- `ShowText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `PDIMAGE_LongerSize`
- `Bjornulf_TextToStringAndSeed`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `CR Text Concatenate`
- `RHHiddenNodes`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1039048886568320`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: ImageReel`、`LoadImage`、`LayerUtility: ImageReelComposit`、`ShowText`、`CLIPTextEncode`、`VAEEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`PDIMAGE_LongerSize`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`SaveImage`、`CR Text Concatenate`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
