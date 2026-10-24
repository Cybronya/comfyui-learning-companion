---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json
name: Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json
hash: c457aa8bf55c00b7
coverage: 0.833333
learned_at: 2026-10-23 11:16:11
nodes: [LoadImage, CLIPLoader, UNETLoader, LoraLoaderModelOnly, FluxKontextMultiReferenceLatentMethod, MarkdownNote, EmptyLatentImage, CR Text, LoadImage, LoadImage, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, TextEncodeQwenImageEditPlus, ImageConcatMulti, VAELoader, KSampler, WujiCleaner, VAEDecode, WujiUpscaler, ImageConcanate, SaveImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 43621481434101, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5三参考图生图_2004195228674387969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `CR Text`
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `ImageConcatMulti`
- `VAELoader`
- `KSampler` ★核心
- `WujiCleaner`
- `VAEDecode` ★核心
- `WujiUpscaler`
- `ImageConcanate`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `43621481434101`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`LoadImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`EmptyLatentImage`、`CR Text`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`ImageConcatMulti`、`VAELoader`、`KSampler`、`WujiCleaner`、`VAEDecode`、`WujiUpscaler`、`ImageConcanate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
