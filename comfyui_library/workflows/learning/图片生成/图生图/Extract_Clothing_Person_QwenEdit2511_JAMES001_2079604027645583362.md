---
key: 图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json
name: Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json
hash: 83de2254b78b0d16
coverage: 0.875
learned_at: 2026-10-23 10:52:34
nodes: [VAEEncode, EmptySD3LatentImage, ImageResizeKJv2, LayerUtility: PurgeVRAM, TextEncodeQwenImageEditPlus, VAEDecode, KSampler, KSampler, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, LayerUtility: PurgeVRAM, CFGNorm, ModelSamplingAuraFlow, LayerUtility: PurgeVRAM, TextEncodeQwenImageEditPlus, VAEDecode, easy imageConcat, ImageStitch, SaveImage, SaveImage, SaveImage, PrimitiveInt, JjkText, PrimitiveInt, MarkdownNote, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 311702291275215, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: PurgeVRAM`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LayerUtility: PurgeVRAM`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `easy imageConcat`
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveInt`
- `JjkText`
- `PrimitiveInt`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `311702291275215`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`VAEEncode`、`EmptySD3LatentImage`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`KSampler`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`easy imageConcat`、`ImageStitch`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
