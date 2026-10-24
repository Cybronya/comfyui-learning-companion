---
key: 图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json
name: Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json
hash: 3ea44f623d25f442
coverage: 0.941176
learned_at: 2026-10-23 11:16:16
nodes: [CLIPLoader, LoraLoaderModelOnly, KSampler, VAEDecode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, SaveImage, EmptyLatentImage, PreviewImage, VAELoader, ConditioningZeroOut, UnetLoaderGGUF, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 908373921508604, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `VAELoader`
- `ConditioningZeroOut`
- `UnetLoaderGGUF` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `908373921508604`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`FluxKontextMultiReferenceLatentMethod`、`SaveImage`、`EmptyLatentImage`、`VAELoader`、`ConditioningZeroOut`、`UnetLoaderGGUF`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
