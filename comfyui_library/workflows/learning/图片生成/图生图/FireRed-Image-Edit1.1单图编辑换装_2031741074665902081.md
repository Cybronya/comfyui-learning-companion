---
key: 图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json
name: FireRed-Image-Edit1.1单图编辑换装_2031741074665902081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json
hash: bea8d18ef39d3559
coverage: 0.95
learned_at: 2026-10-23 10:55:44
nodes: [CLIPLoader, UNETLoader, VAELoader, ConditioningZeroOut, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, VAEDecode, LoadImage, LoadImage, KSampler, SaveImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Int, TextEncodeQwenImageEditPlus, CR Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 998548336731293, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `TextEncodeQwenImageEditPlus`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `998548336731293`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`VAEDecode`、`LoadImage`、`KSampler`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`TextEncodeQwenImageEditPlus`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
