---
key: 图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json
name: Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json
hash: 867983b1da83c6aa
coverage: 0.883721
learned_at: 2026-10-23 11:03:50
nodes: [VAELoader, Note, ModelSamplingSD3, Bjornulf_TextToStringAndSeed, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, VAEEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, PDIMAGE_LongerSize, VAEDecode, SaveImage, SaveImage, VAEDecode, SaveImage, ModelSamplingSD3, PMRF, CLIPTextEncode, KSampler, KSampler, easy cleanGpuUsed, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1, Note, LayerUtility: LoadJoyCaptionBeta1Model, CLIPTextEncode, ShowText|pysssss, CLIPLoader, ShowText|pysssss, LoraLoaderModelOnly, DeepTranslatorTextNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PDIMAGE_LongerSize, Note, ImageConcanate, DeepTranslatorTextNode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 497163970725457, "steps": 20}
---

# 图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `Bjornulf_TextToStringAndSeed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ModelSamplingSD3`
- `PMRF`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: JoyCaptionBeta1`
- `Note`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `CLIPLoader`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `DeepTranslatorTextNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PDIMAGE_LongerSize`
- `Note`
- `ImageConcanate`
- `DeepTranslatorTextNode`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`VAELoader`、`ModelSamplingSD3`、`Bjornulf_TextToStringAndSeed`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAEEncode`、`PDIMAGE_LongerSize`、`VAEDecode`、`SaveImage`、`PMRF`、`CLIPTextEncode`、`KSampler`、`easy cleanGpuUsed`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`CLIPLoader`、`DeepTranslatorTextNode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
