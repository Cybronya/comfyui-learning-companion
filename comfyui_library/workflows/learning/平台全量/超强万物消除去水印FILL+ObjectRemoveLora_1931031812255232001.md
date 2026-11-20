---
key: 平台全量/超强万物消除去水印FILL+ObjectRemoveLora_1931031812255232001.json
name: 超强万物消除去水印FILL+ObjectRemoveLora_1931031812255232001
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/超强万物消除去水印FILL+ObjectRemoveLora_1931031812255232001.json
hash: 95e7a9ff92c97115
coverage: 0.777778
learned_at: 2026-11-14 02:45:52
nodes: [FluxGuidance, ConditioningZeroOut, DifferentialDiffusion, Anything Everywhere, VAEDecode, VAELoader, DifferentialDiffusion, ConditioningZeroOut, FluxGuidance, VAEEncode, SaveImage, Joy_caption_two_load, Joy_caption_two, PreviewBridge, UNETLoader, PreviewImage, SUPIR_Upscale, Image Comparer (rgthree), VAEDecode, LamaRemover, PreviewImage, Note, Fast Groups Muter (rgthree), InpaintModelConditioning, LoraLoaderModelOnly, CLIPTextEncode, easy showAnything, PreviewImage, LoadImage, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, SetLatentNoiseMask, KSampler, KSampler, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 560719103186358, "steps": 28}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/超强万物消除去水印FILL+ObjectRemoveLora_1931031812255232001.json

> 来源文件 `comfyui_library/workflows/平台全量/超强万物消除去水印FILL+ObjectRemoveLora_1931031812255232001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `FluxGuidance`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `VAELoader`
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEEncode` ★核心
- `SaveImage`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `PreviewBridge`
- `UNETLoader` ★核心
- `PreviewImage`
- `SUPIR_Upscale`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LamaRemover`
- `PreviewImage`
- `Note`
- `Fast Groups Muter (rgthree)`
- `InpaintModelConditioning`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `560719103186358`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`FluxGuidance`、`ConditioningZeroOut`、`DifferentialDiffusion`、`VAEDecode`、`VAELoader`、`VAEEncode`、`SaveImage`、`Joy_caption_two_load`、`Joy_caption_two`、`PreviewBridge`、`UNETLoader`、`SUPIR_Upscale`、`LamaRemover`、`InpaintModelConditioning`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`DualCLIPLoader`、`SetLatentNoiseMask`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
