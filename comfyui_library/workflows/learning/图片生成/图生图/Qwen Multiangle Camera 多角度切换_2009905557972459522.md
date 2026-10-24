---
key: 图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json
name: Qwen Multiangle Camera 多角度切换_2009905557972459522
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json
hash: 864ad0a634bf018c
coverage: 0.947368
learned_at: 2026-10-23 11:13:38
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewAny, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, Int, KSampler, VAEEncode, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, UNETLoader, VAEDecode, QwenMultiangleCameraNode, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Int`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `QwenMultiangleCameraNode`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`Int`、`KSampler`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`ConditioningZeroOut`、`UNETLoader`、`VAEDecode`、`QwenMultiangleCameraNode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
