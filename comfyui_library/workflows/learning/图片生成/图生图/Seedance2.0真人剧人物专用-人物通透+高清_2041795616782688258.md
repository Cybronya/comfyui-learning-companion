---
key: 图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json
name: Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json
hash: dc8876afed312e8b
coverage: 0.632184
learned_at: 2026-10-23 11:25:37
nodes: [CLIPLoader, VAELoader, VAEDecode, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, ConditioningZeroOut, SetNode, Any Switch (rgthree), UNETLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, VAELoader, LayerUtility: PurgeVRAM, SetNode, SetNode, GetNode, GetNode, GetNode, JWInteger, Qwen3_VQA, PlaySound|pysssss, ShowText|pysssss, SetNode, SetNode, CR String To Number, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ImpactSwitch, LoraLoaderModelOnly, GetNode, CR Text, CR Text, GetNode, UNETLoader, SetNode, PlaySound|pysssss, PlaySound|pysssss, GetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, SaveImage, CLIPLoader, LayerUtility: PurgeVRAM V2, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, VAEDecode, ImageScaleToTotalPixels, SetNode, CLIPTextEncode, VAELoader, ConditioningZeroOut, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, Flux2Scheduler, GetImageSize, EmptyFlux2LatentImage, ColorMatch, ImageSharpen, GetNode, Image Comparer (rgthree), CR Text, SetNode, Fast Groups Muter (rgthree), KSampler, GetNode, Reroute, Reroute, GetNode, ImageConcanate, ImageConcanate, SetNode, GetNode, GetNode, ImageConcanate, SetNode, PreviewImage, LoadImage, MarkdownNote, Image Comparer (rgthree), LoadImage, SaveImage, PrimitiveFloat]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 88888888, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `Qwen3_VQA`
- `PlaySound|pysssss`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `CR String To Number`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `CR Text`
- `CR Text`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `GetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `SaveImage`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM V2`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `Flux2Scheduler`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `ColorMatch`
- `ImageSharpen`
- `GetNode`
- `Image Comparer (rgthree)`
- `CR Text`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `ImageConcanate`
- `ImageConcanate`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `PrimitiveFloat`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `88888888`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **63%**（55/87）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: PurgeVRAM`、`JWInteger`、`Qwen3_VQA`、`PlaySound|pysssss`、`CR String To Number`、`LoraLoaderModelOnly`、`CR Text`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`SaveImage`、`LayerUtility: PurgeVRAM V2`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ImageScaleToTotalPixels`、`ReferenceLatent`、`CFGGuider`、`Flux2Scheduler`、`GetImageSize`、`EmptyFlux2LatentImage`、`ColorMatch`、`ImageSharpen`、`ImageConcanate`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
