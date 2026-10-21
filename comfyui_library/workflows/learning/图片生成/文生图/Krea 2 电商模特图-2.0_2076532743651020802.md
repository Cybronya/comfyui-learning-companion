---
key: 图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json
name: Krea 2 电商模特图-2.0_2076532743651020802
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json
hash: 5edfb7cadf0d5390
coverage: 0.883721
learned_at: 2026-10-20 00:19:10
nodes: [VAELoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, CLIPLoader, Dapao_LlamaCaptionOptions, Fast Groups Bypasser (rgthree), easy showAnything, CR Text, RegexReplace, String Literal, ImpactInt, ImpactInt, CR Prompt List, easy showAnything, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcatMulti, ImageConcatMulti, ImageFromBatch, ImageConcatMulti, SaveImage, Dapao_LlamaCaption, UNETLoader, LoraLoaderModelOnly, LoadImage, KSampler, VAEDecodeTiled, Image Comparer (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, ResizeImageMaskNode, VAEEncodeTiled, SeedVR2Preprocess, UNETLoader, VAELoader, CR Batch Images From List, SaveImage, KSampler, VAEDecode, SaveImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler_ancestral", "scheduler": "bong_tangent", "seed": 12, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `Dapao_LlamaCaptionOptions`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `CR Text`
- `RegexReplace`
- `String Literal`
- `ImpactInt`
- `ImpactInt`
- `CR Prompt List`
- `easy showAnything`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageConcatMulti`
- `SaveImage`
- `Dapao_LlamaCaption`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `ResizeImageMaskNode`
- `VAEEncodeTiled` ★核心
- `SeedVR2Preprocess`
- `UNETLoader` ★核心
- `VAELoader`
- `CR Batch Images From List`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `12`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`CLIPLoader`、`Dapao_LlamaCaptionOptions`、`CR Text`、`RegexReplace`、`String Literal`、`ImpactInt`、`CR Prompt List`、`ImageFromBatch`、`ImageConcatMulti`、`SaveImage`、`Dapao_LlamaCaption`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`KSampler`、`VAEDecodeTiled`、`SeedVR2Conditioning`、`SeedVR2PostProcessing`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`SeedVR2Preprocess`、`CR Batch Images From List`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
