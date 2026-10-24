---
key: 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json
name: 史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json
hash: 739eeb18ec474e92
coverage: 0.707317
learned_at: 2026-10-23 12:36:13
nodes: [GetNode, SetNode, SetNode, SetNode, Note, MarkdownNote, GetNode, GetNode, SetNode, VAELoader, CLIPLoader, VAEEncode, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, GetNode, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEdit, LoadImage, KSampler, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, CLIPLoader, VAELoader, RunningHub Deepcleaner, CLIPTextEncode, KSamplerAdvanced, VAEDecode, VAEEncode, VAEDecode, KSamplerAdvanced, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, CLIPTextEncode, SaveImage, LoadImage, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "res_2m", "seed": "enable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）+去除横纹_2012875763338448897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEdit`
- `LoadImage`
- `KSampler` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `RunningHub Deepcleaner`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `res_2m`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **71%**（29/41）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEEncode`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEdit`、`LoadImage`、`KSampler`、`FluxKontextMultiReferenceLatentMethod`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`RunningHub Deepcleaner`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`UNETLoader`、`SaveImage`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
