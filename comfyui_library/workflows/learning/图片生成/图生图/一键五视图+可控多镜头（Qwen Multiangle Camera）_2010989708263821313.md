---
key: 图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json
name: 一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json
hash: 302f5f51f1c676ae
coverage: 0.894737
learned_at: 2026-10-23 11:54:35
nodes: [LoadImage, UNETLoader, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, CLIPLoader, VAELoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, KSampler, MarkdownNote, LoadImage, MarkdownNote, easy showAnything, easy promptList, Int, EmptySD3LatentImage, ImageScaleToTotalPixels, VAEEncode, VAEDecode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, Int, InversionDemoLazySwitch, Compare, Int, AspectRatio, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `CLIPLoader`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `easy showAnything`
- `easy promptList`
- `Int`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `Int`
- `InversionDemoLazySwitch`
- `Compare`
- `Int`
- `AspectRatio`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`LoadImage`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`PlaySound|pysssss`、`CLIPLoader`、`VAELoader`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`easy promptList`、`Int`、`EmptySD3LatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`VAEDecode`、`QwenMultiangleCameraNode`、`InversionDemoLazySwitch`、`Compare`、`AspectRatio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
