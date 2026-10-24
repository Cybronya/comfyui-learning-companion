---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162.json
name: Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162.json
hash: 614985fb899b8257
coverage: 0.846154
learned_at: 2026-10-23 11:16:12
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, CLIPLoader, UNETLoader, LoraLoaderModelOnly, FluxKontextMultiReferenceLatentMethod, MarkdownNote, EmptyLatentImage, LoadImage, SaveImage, PreviewImage, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, ImageConcatMulti, ImageConcanate, VAELoader, CR Text, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 433580952693140, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三图参考图生图_2043587733939036162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `ImageConcanate`
- `VAELoader`
- `CR Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `433580952693140`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`EmptyLatentImage`、`LoadImage`、`SaveImage`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ImageConcatMulti`、`ImageConcanate`、`VAELoader`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
