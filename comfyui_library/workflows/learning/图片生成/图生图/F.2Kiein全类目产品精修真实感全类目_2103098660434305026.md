---
key: 图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json
name: F.2Kiein全类目产品精修真实感全类目_2103098660434305026
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json
hash: 8e25658116967a1d
coverage: 0.84375
learned_at: 2026-10-21 00:38:56
nodes: [ConditioningZeroOut, VAEEncode, VAELoader, KSampler, ReferenceLatent, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, UNETLoader, Image Comparer (rgthree), ConditioningZeroOut, VAEEncode, VAELoader, KSampler, ReferenceLatent, VAEDecode, SaveImage, Note, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly, RHUploadZip_V2, HAIGC_SaveImagesToZip, Note, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1072921346137388, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `RHUploadZip_V2`
- `HAIGC_SaveImagesToZip`
- `Note`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1072921346137388`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`VAELoader`、`KSampler`、`ReferenceLatent`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`RHUploadZip_V2`、`HAIGC_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
