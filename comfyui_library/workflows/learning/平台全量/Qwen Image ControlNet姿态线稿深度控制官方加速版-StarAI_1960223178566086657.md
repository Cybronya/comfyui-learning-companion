---
key: 平台全量/Qwen Image ControlNet姿态线稿深度控制官方加速版-StarAI_1960223178566086657.json
name: Qwen Image ControlNet姿态线稿深度控制官方加速版-StarAI_1960223178566086657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image ControlNet姿态线稿深度控制官方加速版-StarAI_1960223178566086657.json
hash: f868cf47e790123d
coverage: 0.861111
learned_at: 2026-11-14 00:50:09
nodes: [Note Plus (mtb), VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, VAEDecode, CLIPTextEncode, ReferenceLatent, PreviewImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, easy clearCacheAll, ShowText|pysssss, LayerUtility: JoyCaptionBeta1, ReferenceLatent, easy textSwitch, Int, SaveImage, MarkdownNote, CLIPLoader, AIO_Preprocessor, ImpactSwitch, Int, ImageScaleToTotalPixels, easy imagePixelPerfect, VAEEncode, ModelSamplingAuraFlow, CLIPTextEncode, AIO_Preprocessor, AIO_Preprocessor, Note, KSampler, LoraLoaderModelOnly, UNETLoader, ModelPatchTorchSettings, LoadImage, CR Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 166111271305187, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen Image ControlNet姿态线稿深度控制官方加速版-StarAI_1960223178566086657.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image ControlNet姿态线稿深度控制官方加速版-StarAI_1960223178566086657.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Note Plus (mtb)`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `PreviewImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `easy clearCacheAll`
- `ShowText|pysssss`
- `LayerUtility: JoyCaptionBeta1`
- `ReferenceLatent`
- `easy textSwitch`
- `Int`
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `Int`
- `ImageScaleToTotalPixels`
- `easy imagePixelPerfect`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Note`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `LoadImage`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `166111271305187`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`Note Plus (mtb)`、`VAELoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAEDecode`、`CLIPTextEncode`、`ReferenceLatent`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`easy clearCacheAll`、`LayerUtility: JoyCaptionBeta1`、`easy textSwitch`、`Int`、`SaveImage`、`CLIPLoader`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`easy imagePixelPerfect`、`VAEEncode`、`ModelSamplingAuraFlow`、`KSampler`、`UNETLoader`、`ModelPatchTorchSettings`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
