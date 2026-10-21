---
key: 图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json
name: image2.5噪点色斑处理放大工作流_2105122148300967938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json
hash: d0d9757b8ccd40fd
coverage: 0.777778
learned_at: 2026-10-21 00:45:30
nodes: [ImageScaleToMaxDimension, VAEEncode, RepeatLatentBatch, Florence2Run, easy ifElse, TextConcatenator, CLIPTextEncode, ConditioningZeroOut, VAEDecode, UNETLoader, VAELoader, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, TextConcatenator, PreviewTextNode, VAELoader, UNETLoader, ImageScaleToMaxDimension, LoadImage, Florence2ModelLoader, KSampler, PrimitiveNode, CLIPLoader, PrimitiveNode, PrimitiveNode, Image Comparer (rgthree), KSampler, PrimitiveNode, PrimitiveNode, SaveImage, ModelSamplingAuraFlow, PrimitiveNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.24000000000000005, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 276007575494159, "steps": 3}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ImageScaleToMaxDimension`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `Florence2Run`
- `easy ifElse`
- `TextConcatenator`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2Conditioning`
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `SaveImage`
- `TextConcatenator`
- `PreviewTextNode`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScaleToMaxDimension`
- `LoadImage`
- `Florence2ModelLoader`
- `KSampler` ★核心
- `PrimitiveNode`
- `CLIPLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `PrimitiveNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `276007575494159`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.24000000000000005`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`ImageScaleToMaxDimension`、`VAEEncode`、`RepeatLatentBatch`、`Florence2Run`、`TextConcatenator`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`SaveImage`、`PreviewTextNode`、`LoadImage`、`Florence2ModelLoader`、`KSampler`、`CLIPLoader`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
