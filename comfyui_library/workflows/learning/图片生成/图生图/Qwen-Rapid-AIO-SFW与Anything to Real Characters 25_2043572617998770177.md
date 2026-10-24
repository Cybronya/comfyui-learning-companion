---
key: 图片生成/图生图/Qwen-Rapid-AIO-SFW与Anything to Real Characters 25_2043572617998770177.json
name: Qwen-Rapid-AIO-SFW与Anything to Real Characters 25_2043572617998770177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Rapid-AIO-SFW与Anything to Real Characters 25_2043572617998770177.json
hash: 6574e44986d95113
coverage: 0.75
learned_at: 2026-10-23 11:17:31
nodes: [Reroute, Reroute, KSampler, VAEDecode, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, VAEEncode, TextEncodeQwenImageEdit, Reroute, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, CheckpointLoaderSimple, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, TT_img_enc, SaveImage, Fast Groups Bypasser (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v20.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 357642460733096, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Rapid-AIO-SFW与Anything to Real Characters 25_2043572617998770177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Rapid-AIO-SFW与Anything to Real Characters 25_2043572617998770177.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEdit`
- `Reroute`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `TT_img_enc`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `357642460733096`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.0.safetensors`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`KSampler`、`VAEDecode`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`TextEncodeQwenImageEdit`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`TT_img_enc`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、CFGNorm、FluxKontextMultiReferenceLatentMethod、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
