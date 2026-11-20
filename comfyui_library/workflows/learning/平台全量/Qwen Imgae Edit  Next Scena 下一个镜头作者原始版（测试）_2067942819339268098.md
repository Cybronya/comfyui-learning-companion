---
key: 平台全量/Qwen Imgae Edit  Next Scena 下一个镜头作者原始版（测试）_2067942819339268098.json
name: Qwen Imgae Edit  Next Scena 下一个镜头作者原始版（测试）_2067942819339268098
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Imgae Edit  Next Scena 下一个镜头作者原始版（测试）_2067942819339268098.json
hash: 28ef12ee9d193b17
coverage: 0.818182
learned_at: 2026-11-14 00:50:21
nodes: [DualCLIPLoader, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, CLIPTextEncode, CR Text, ProcessString, easy promptLine, ImageScaleToTotalPixels, CLIPLoader, Note, EmptySD3LatentImage, MarkdownNote, CFGNorm, ModelSamplingAuraFlow, KSampler, ShowText|pysssss, ShowText|pysssss, VAEDecode, ConditioningZeroOut, KSampler, VAEDecode, SaveImage, Text Load Line From File, ImageScaleBy, SaveImage, PreviewAny, easy showAnything, Text Multiline, Text Multiline, MasqueradeIncrementer, easy rangeInt, ImpactInt, UNETLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, VAEEncode, easy showAnything, LoadImage, LoadImage, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 943556351579141, "steps": 30}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen Imgae Edit  Next Scena 下一个镜头作者原始版（测试）_2067942819339268098.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Imgae Edit  Next Scena 下一个镜头作者原始版（测试）_2067942819339268098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `CR Text`
- `ProcessString`
- `easy promptLine`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `Note`
- `EmptySD3LatentImage`
- `MarkdownNote`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Text Load Line From File`
- `ImageScaleBy`
- `SaveImage`
- `PreviewAny`
- `easy showAnything`
- `Text Multiline`
- `Text Multiline`
- `MasqueradeIncrementer`
- `easy rangeInt`
- `ImpactInt`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `943556351579141`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`DualCLIPLoader`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`CR Text`、`ProcessString`、`easy promptLine`、`ImageScaleToTotalPixels`、`CLIPLoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`Text Load Line From File`、`ImageScaleBy`、`Text Multiline`、`MasqueradeIncrementer`、`easy rangeInt`、`ImpactInt`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
