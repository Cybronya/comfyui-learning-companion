---
key: 图片生成/图生图/AI狂徒-人物姿势调整 极致参考-发布版1.0_2057328769886670849.json
name: AI狂徒-人物姿势调整 极致参考-发布版1.0_2057328769886670849
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI狂徒-人物姿势调整 极致参考-发布版1.0_2057328769886670849.json
hash: c8642a77c2f7b3cc
coverage: 0.734266
learned_at: 2026-10-23 10:50:46
nodes: [SaveImage, CFGNorm, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, LayerUtility: PurgeVRAM, ConditioningZeroOut, ModelSamplingAuraFlow, CFGNorm, VAELoader, CLIPLoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, LayerUtility: PurgeVRAM, ConditioningZeroOut, VAEEncode, ModelSamplingAuraFlow, GetNode, KSampler, CFGNorm, VAELoader, CLIPLoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, LayerUtility: PurgeVRAM, ConditioningZeroOut, LoadSAM3Model, EmptyImage, LoadSAM3DBodyModel, SAM3DBodyProcessToJson, SAM3Segmentation, ttN text, GetNode, TextEncodeQwenImageEditPlus, CheckpointLoaderSimple, CheckpointLoaderSimple, CheckpointLoaderSimple, FL_SendToDiscordWebhook, FL_SendToDiscordWebhook, FL_SendToDiscordWebhook, DWPreprocessor, SAM3DBodyRenderFromJson, LoraLoaderModelOnly, SaveImage, ImageResizeKJv2, ModelSamplingAuraFlow, Text Concatenate, VAELoader, CLIPLoader, LoadImage, TextEncodeQwenImageEditPlus, GetNode, VAEEncode, CheckpointLoaderSimple, LoraLoaderModelOnly, KSampler, TextEncodeQwenImageEditPlus, Text Concatenate, Reroute, JjkText, TT_img_enc, TT_img_enc, VAEEncode, Reroute, ZML_AnyTypeSwitch, LayerUtility: ImageScaleByAspectRatio V2, RMBG, SetNode, RMBG, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, PreviewImage, PreviewImage, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, ZML_AnyTypeSwitch, LayerUtility: ImageScaleByAspectRatio V2, RMBG, RMBG, ZML_AnyTypeSwitch, GetNode, JjkText, DWPreprocessor, JjkText, JjkText, ZML_AnyTypeSwitch, GetNode, VAEDecode, SetNode, SetNode, VAEDecode, VAEDecode, SetNode, ImageBatchToList_, ImageBatchToList_, SetNode, ZML_SwitchOutputFive, SetNode, SetNode, JWInteger, GetNode, GetNode, SetNode, ZML_SwitchOutputFive, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ZML_AnyTypeSwitch, Reroute, LayerUtility: ImageScaleByAspectRatio V2, RMBG, Reroute, RMBG, SaveImage, SaveImage, GetNode, ImageBatchToList_, ZML_SwitchOutputFive, ZML_SwitchOutputFive, GetNode, GetNode, GetNode, ZML_SwitchOutputFive, SaveImage, SaveImage, Text Concatenate, SetNode, GetNode, JjkText, LoraLoaderModelOnly, KSampler, LoadImage, TT_img_enc, LoraLoaderModelOnly, ZML_BooleanSwitch, CheckpointLoaderSimple, LoraLoaderModelOnly, CheckpointLoaderSimple, JWInteger, LoadImage, JjkText, JWInteger]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "new_Qwen-Rapid-AIO-NSFW-v23.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 498132578903492, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/AI狂徒-人物姿势调整 极致参考-发布版1.0_2057328769886670849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI狂徒-人物姿势调整 极致参考-发布版1.0_2057328769886670849.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
- `SaveImage`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `LayerUtility: PurgeVRAM`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `LayerUtility: PurgeVRAM`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `GetNode`
- `KSampler` ★核心
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `LayerUtility: PurgeVRAM`
- `ConditioningZeroOut`
- `LoadSAM3Model`
- `EmptyImage`
- `LoadSAM3DBodyModel`
- `SAM3DBodyProcessToJson`
- `SAM3Segmentation`
- `ttN text`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `FL_SendToDiscordWebhook`
- `FL_SendToDiscordWebhook`
- `FL_SendToDiscordWebhook`
- `DWPreprocessor`
- `SAM3DBodyRenderFromJson`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `ImageResizeKJv2`
- `ModelSamplingAuraFlow`
- `Text Concatenate`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `Text Concatenate`
- `Reroute`
- `JjkText`
- `TT_img_enc`
- `TT_img_enc`
- `VAEEncode` ★核心
- `Reroute`
- `ZML_AnyTypeSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `SetNode`
- `RMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `ZML_AnyTypeSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `RMBG`
- `ZML_AnyTypeSwitch`
- `GetNode`
- `JjkText`
- `DWPreprocessor`
- `JjkText`
- `JjkText`
- `ZML_AnyTypeSwitch`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `ImageBatchToList_`
- `ImageBatchToList_`
- `SetNode`
- `ZML_SwitchOutputFive`
- `SetNode`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `SetNode`
- `ZML_SwitchOutputFive`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ZML_AnyTypeSwitch`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `Reroute`
- `RMBG`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `ImageBatchToList_`
- `ZML_SwitchOutputFive`
- `ZML_SwitchOutputFive`
- `GetNode`
- `GetNode`
- `GetNode`
- `ZML_SwitchOutputFive`
- `SaveImage`
- `SaveImage`
- `Text Concatenate`
- `SetNode`
- `GetNode`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `TT_img_enc`
- `LoraLoaderModelOnly` ★核心
- `ZML_BooleanSwitch`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `JWInteger`
- `LoadImage`
- `JjkText`
- `JWInteger`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `498132578903492`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `new_Qwen-Rapid-AIO-NSFW-v23.safetensors`

## 知识

覆盖率 **73%**（105/143）

**有卡**：`SaveImage`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`LayerUtility: PurgeVRAM`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`VAEEncode`、`KSampler`、`LoadSAM3Model`、`EmptyImage`、`LoadSAM3DBodyModel`、`SAM3DBodyProcessToJson`、`SAM3Segmentation`、`ttN text`、`TextEncodeQwenImageEditPlus`、`CheckpointLoaderSimple`、`FL_SendToDiscordWebhook`、`DWPreprocessor`、`SAM3DBodyRenderFromJson`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`Text Concatenate`、`LoadImage`、`TT_img_enc`、`ZML_AnyTypeSwitch`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`GetImageSize`、`VAEDecode`、`ImageBatchToList_`、`ZML_SwitchOutputFive`、`JWInteger`、`ZML_BooleanSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
