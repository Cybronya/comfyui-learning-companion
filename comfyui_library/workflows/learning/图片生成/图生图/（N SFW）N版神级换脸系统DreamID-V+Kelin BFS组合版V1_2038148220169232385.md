---
key: 图片生成/图生图/（N SFW）N版神级换脸系统DreamID-V+Kelin BFS组合版V1_2038148220169232385.json
name: （N SFW）N版神级换脸系统DreamID-V+Kelin BFS组合版V1_2038148220169232385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（N SFW）N版神级换脸系统DreamID-V+Kelin BFS组合版V1_2038148220169232385.json
hash: 425868c3c7338bad
coverage: 0.913043
learned_at: 2026-10-23 13:37:15
nodes: [RunningHub_DreamID-V_Loader, Note, Float, Note, ImageConcatMulti, Float to Int, ImageScaleToTotalPixels, VAEEncode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, LayerUtility: PurgeVRAM V2, CLIPTextEncode, ReferenceLatent, ReferenceLatent, RepeatImageBatch, JWInteger, CreateVideo, GetVideoComponents, easy showAnything, RunningHub_DreamID-V_Sampler, ImageFromBatch+, UNETLoader, CLIPLoader, VAELoader, CR Prompt Text, SaveImage, SaveImage, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, DuckHideNode, TT_img_enc_v2, CR Text, SaveImage, VAEDecode, KSampler, LoadImage, LoadImage, SaveImage, TT_img_enc, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 899486910053537, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（N SFW）N版神级换脸系统DreamID-V+Kelin BFS组合版V1_2038148220169232385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（N SFW）N版神级换脸系统DreamID-V+Kelin BFS组合版V1_2038148220169232385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `RunningHub_DreamID-V_Loader`
- `Note`
- `Float`
- `Note`
- `ImageConcatMulti`
- `Float to Int`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RepeatImageBatch`
- `JWInteger`
- `CreateVideo`
- `GetVideoComponents`
- `easy showAnything`
- `RunningHub_DreamID-V_Sampler` ★核心
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DuckHideNode`
- `TT_img_enc_v2`
- `CR Text`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `TT_img_enc`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `899486910053537`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`RunningHub_DreamID-V_Loader`、`Float`、`ImageConcatMulti`、`Float to Int`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`RepeatImageBatch`、`JWInteger`、`CreateVideo`、`GetVideoComponents`、`RunningHub_DreamID-V_Sampler`、`ImageFromBatch+`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`DuckHideNode`、`TT_img_enc_v2`、`CR Text`、`VAEDecode`、`KSampler`、`LoadImage`、`TT_img_enc`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
