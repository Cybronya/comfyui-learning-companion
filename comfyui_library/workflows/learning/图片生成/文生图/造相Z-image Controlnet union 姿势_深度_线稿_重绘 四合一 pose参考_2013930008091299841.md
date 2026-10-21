---
key: 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json
name: 造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json
hash: ff80c231336331b3
coverage: 0.488636
learned_at: 2026-10-19 22:16:09
nodes: [ImageSmartSharpen+, GetNode, UNETLoader, CLIPLoader, VAELoader, VAEDecode, SetNode, GetNode, CLIPTextEncode, Reroute, Reroute, VAEDecode, SetNode, AIO_Preprocessor, AIO_Preprocessor, DWPreprocessor, ImageSmartSharpen+, GetNode, SetNode, easy seed, GetNode, GetNode, CR Prompt Text, JWInteger, SetNode, GetNode, LayerUtility: TextJoin, PrimitiveNode, easy showAnything, easy showAnything, easy showAnything, JWInteger, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, PreviewImage, LoraLoaderModelOnly, LatentPixelScale, UpscaleModelLoader, easy showAnything, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, AILab_QwenVL, LoadImage, easy imageRemBg, GetNode, SetNode, KSampler, GetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Note, ConditioningZeroOut, Note, SetNode, SetNode, Note, Anything Everywhere3, Reroute, SetNode, VAEEncode, RepeatLatentBatch, GetNode, GetNode, RebatchLatents, ImpactSwitch, GetNode, ZImageFunControlnet, MuterSwitcher, GetNode, GetNode, GetNode, Note, easy boolean, LoadImage, GetNode, GetImageSize, ImpactSwitch, ImageResizeKJv2, ModelPatchLoader, SaveImage, KSampler, SaveImage, AILab_QwenVL, AILab_QwenVL]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 1030454734910631, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `ImageSmartSharpen+`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `SetNode`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `ImageSmartSharpen+`
- `GetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `GetNode`
- `CR Prompt Text`
- `JWInteger`
- `SetNode`
- `GetNode`
- `LayerUtility: TextJoin`
- `PrimitiveNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `JWInteger`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LatentPixelScale`
- `UpscaleModelLoader`
- `easy showAnything`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `AILab_QwenVL`
- `LoadImage`
- `easy imageRemBg`
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ConditioningZeroOut`
- `Note`
- `SetNode`
- `SetNode`
- `Note`
- `Anything Everywhere3`
- `Reroute`
- `SetNode`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `GetNode`
- `GetNode`
- `RebatchLatents`
- `ImpactSwitch`
- `GetNode`
- `ZImageFunControlnet`
- `MuterSwitcher`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `easy boolean`
- `LoadImage`
- `GetNode`
- `GetImageSize`
- `ImpactSwitch`
- `ImageResizeKJv2`
- `ModelPatchLoader`
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `AILab_QwenVL`
- `AILab_QwenVL`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1030454734910631`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **49%**（43/88）

**有卡**：`ImageSmartSharpen+`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`AIO_Preprocessor`、`DWPreprocessor`、`easy seed`、`CR Prompt Text`、`JWInteger`、`LayerUtility: TextJoin`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`LatentPixelScale`、`UpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`AILab_QwenVL`、`LoadImage`、`easy imageRemBg`、`KSampler`、`ConditioningZeroOut`、`VAEEncode`、`RepeatLatentBatch`、`RebatchLatents`、`ZImageFunControlnet`、`MuterSwitcher`、`easy boolean`、`GetImageSize`、`ImageResizeKJv2`、`ModelPatchLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
