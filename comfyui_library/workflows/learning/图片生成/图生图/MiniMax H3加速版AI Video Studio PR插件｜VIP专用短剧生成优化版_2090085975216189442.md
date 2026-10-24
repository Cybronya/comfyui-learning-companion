---
key: 图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json
name: MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json
hash: 6ef51ad194024677
coverage: 0.898305
learned_at: 2026-10-23 11:09:22
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, UpscaleModelLoader, ComfyMathExpression, VAELoader, VAELoader, UNETLoader, CLIPLoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, PathchSageAttentionKJ, EasyCache, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ImageUpscaleWithModel, MiniMaxH3ReferenceToVideo, CreateVideo, SaveVideo, ResolutionSelector, PrimitiveFloat, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `UpscaleModelLoader`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `PathchSageAttentionKJ`
- `EasyCache`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ImageUpscaleWithModel`
- `MiniMaxH3ReferenceToVideo`
- `CreateVideo`
- `SaveVideo`
- `ResolutionSelector`
- `PrimitiveFloat`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（53/59）

**有卡**：`LoadImage`、`UpscaleModelLoader`、`ComfyMathExpression`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`PathchSageAttentionKJ`、`EasyCache`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`ImageUpscaleWithModel`、`MiniMaxH3ReferenceToVideo`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`CR Prompt Text`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
