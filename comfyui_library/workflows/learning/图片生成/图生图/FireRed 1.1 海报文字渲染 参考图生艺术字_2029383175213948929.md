---
key: 图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json
name: FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json
hash: 9d87813da29e8582
coverage: 0.666667
learned_at: 2026-10-23 10:55:23
nodes: [CFGNorm, ModelSamplingAuraFlow, Any Switch (rgthree), GetNode, GetNode, TextEncodeQwenImageEditPlus, JjkText, Note, SetNode, SetNode, AspectRatio, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, VAEEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPLoader, VAELoader, SaveImage, LoadImage, Image Comparer (rgthree), VAEDecode, LoraLoaderModelOnly, ImageResize+, ImageResize+, LoadImage, KSampler, ZML_AddSolidColorBackground, ImageResize+, JjkText, LayerMask: SegmentAnythingUltra V2, AlphaChanelRemove, PreviewImage, LoadImage, LoraLoaderModelOnly, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 696205950362923, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `JjkText`
- `Note`
- `SetNode`
- `SetNode`
- `AspectRatio`
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `KSampler` ★核心
- `ZML_AddSolidColorBackground`
- `ImageResize+`
- `JjkText`
- `LayerMask: SegmentAnythingUltra V2`
- `AlphaChanelRemove`
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `696205950362923`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（24/36）

**有卡**：`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`AspectRatio`、`EmptySD3LatentImage`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`VAEDecode`、`LoraLoaderModelOnly`、`ImageResize+`、`KSampler`、`ZML_AddSolidColorBackground`、`LayerMask: SegmentAnythingUltra V2`、`AlphaChanelRemove`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
