---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json
name: Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json
hash: 517e096433a4777c
coverage: 0.851852
learned_at: 2026-10-23 11:16:11
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LoraLoaderModelOnly, FluxKontextMultiReferenceLatentMethod, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, ConditioningZeroOut, VAELoader, TextEncodeQwenImageEditPlus, UNETLoader, CLIPLoader, ImageConcanate, SeedVR2VideoUpscaler, PreviewImage, SaveImage, LayerUtility: PurgeVRAM V2, ImageConcatMulti, CR Text, EmptyLatentImage, PreviewImage, SaveImage, VAEDecode, Fast Groups Muter (rgthree), LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 663273216901562, "steps": 8, "width": 2752}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2009913119514042370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `LoadImage`
- `ConditioningZeroOut`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageConcanate`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `CR Text`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `663273216901562`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2752`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`LoadImage`、`ConditioningZeroOut`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`CLIPLoader`、`ImageConcanate`、`SeedVR2VideoUpscaler`、`SaveImage`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`CR Text`、`EmptyLatentImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
