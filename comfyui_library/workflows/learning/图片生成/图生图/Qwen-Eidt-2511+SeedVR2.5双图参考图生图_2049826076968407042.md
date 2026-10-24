---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042.json
name: Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042.json
hash: b6575faf807bfaed
coverage: 0.916667
learned_at: 2026-10-23 11:16:13
nodes: [SeedVR2LoadVAEModel, CLIPLoader, UNETLoader, LoraLoaderModelOnly, FluxKontextMultiReferenceLatentMethod, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, TextEncodeQwenImageEditPlus, VAEDecode, LayerUtility: PurgeVRAM V2, ImageConcatMulti, VAELoader, LoadImage, LoadImage, CompressImages, SaveImage, CR Text, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), KSampler, ImageConcanate, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 1103295246284309, "steps": 6, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5双图参考图生图_2049826076968407042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SeedVR2LoadVAEModel`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `EmptyLatentImage` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `CompressImages`
- `SaveImage`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `ImageConcanate`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `1103295246284309`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`SeedVR2LoadVAEModel`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`EmptyLatentImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`VAELoader`、`LoadImage`、`CompressImages`、`SaveImage`、`CR Text`、`KSampler`、`ImageConcanate`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
