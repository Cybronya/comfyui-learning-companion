---
key: 图片生成/文生图/造相Z-image Controlnet union_2016406271590666241.json
name: 造相Z-image Controlnet union_2016406271590666241
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/造相Z-image Controlnet union_2016406271590666241.json
hash: f25968c67f87f7b4
coverage: 0.935484
learned_at: 2026-10-19 22:16:10
nodes: [UNETLoader, Reroute, LoraLoaderModelOnly, ModelPatchLoader, CLIPLoader, VAELoader, LoadImage, ConditioningZeroOut, VAEDecode, SaveImage, KSampler, EmptyLatentImage, CLIPTextEncode, Text, ZImageFunControlnet, AIO_Preprocessor, UNETLoader, Reroute, CLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, KSampler, EmptyLatentImage, CLIPTextEncode, ZImageFunControlnet, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, SaveImage, Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "heun", "scheduler": "beta", "seed": 1030454734910631, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/造相Z-image Controlnet union_2016406271590666241.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/造相Z-image Controlnet union_2016406271590666241.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `Text`
- `ZImageFunControlnet`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ZImageFunControlnet`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `SaveImage`
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1030454734910631`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`Text`、`ZImageFunControlnet`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
