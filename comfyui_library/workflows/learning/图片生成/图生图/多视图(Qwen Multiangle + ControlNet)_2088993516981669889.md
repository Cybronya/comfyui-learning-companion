---
key: 图片生成/图生图/多视图(Qwen Multiangle + ControlNet)_2088993516981669889.json
name: 多视图(Qwen Multiangle + ControlNet)_2088993516981669889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多视图(Qwen Multiangle + ControlNet)_2088993516981669889.json
hash: 731b0e0d4623f681
coverage: 0.96
learned_at: 2026-10-23 12:45:33
nodes: [Getter, Getter, Getter, Getter, Getter, easy showAnything, easy promptList, easy positive, easy promptConcat, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Getter, Getter, Getter, Setter, Getter, LoadImage, LoadImage, ImageScaleToTotalPixels, VAEEncode, Getter, Setter, ImageBatchMulti, easy imageBatchToImageList, DWPreprocessor, Setter, VAELoader, ControlNetLoader, CLIPLoader, CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, VAEDecode, Getter, Getter, Getter, ControlNetApplyAdvanced, SaveImage, Setter, Setter, Setter, Setter, LoadImage, LoadImage, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 897520617280147, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多视图(Qwen Multiangle + ControlNet)_2088993516981669889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多视图(Qwen Multiangle + ControlNet)_2088993516981669889.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `easy showAnything`
- `easy promptList`
- `easy positive`
- `easy promptConcat`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Getter`
- `Getter`
- `Getter`
- `Setter`
- `Getter`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `Getter`
- `Setter`
- `ImageBatchMulti`
- `easy imageBatchToImageList`
- `DWPreprocessor`
- `Setter`
- `VAELoader`
- `ControlNetLoader`
- `CLIPLoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Getter`
- `Getter`
- `Getter`
- `ControlNetApplyAdvanced` ★核心
- `SaveImage`
- `Setter`
- `Setter`
- `Setter`
- `Setter`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `897520617280147`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **96%**（48/50）

**有卡**：`Getter`、`easy promptList`、`easy positive`、`easy promptConcat`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`Setter`、`LoadImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`ImageBatchMulti`、`easy imageBatchToImageList`、`DWPreprocessor`、`VAELoader`、`ControlNetLoader`、`CLIPLoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`VAEDecode`、`ControlNetApplyAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
