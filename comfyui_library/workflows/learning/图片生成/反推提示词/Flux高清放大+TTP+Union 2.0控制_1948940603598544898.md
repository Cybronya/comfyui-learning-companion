---
key: 图片生成/反推提示词/Flux高清放大+TTP+Union 2.0控制_1948940603598544898.json
name: Flux高清放大+TTP+Union 2.0控制_1948940603598544898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Flux高清放大+TTP+Union 2.0控制_1948940603598544898.json
hash: 46d48eb0bae1ebd3
coverage: 0.759259
learned_at: 2026-10-26 01:45:09
nodes: [CLIPTextEncode, SetUnionControlNetType, PreviewImage, easy showAnything, PreviewImage, PreviewImage, CFGGuider, ConditioningCombine, VAEEncode, RandomNoise, FluxGuidance, TTP_Image_Tile_Batch, ImageUpscaleWithModel, ImageResize+, ImageListToImageBatch, TTP_Tile_image_size, ImageScaleToTotalPixels, TTP_Image_Assy, ImpactImageBatchToImageList, VAEDecodeTiled, KSamplerSelect, BasicScheduler, Note, PreviewImage, Reroute, PreviewImage, ConditioningZeroOut, ControlNetApplyAdvanced, SetUnionControlNetType, SaveImage, Image Comparer (rgthree), Reroute, Reroute, ControlNetApplyAdvanced, Joy_caption_two_load, DualCLIPLoader, LoraLoader, ControlNetLoader, StringFunction|pysssss, ShowText|pysssss, Reroute, CLIPTextEncodeFlux, LoadImage, UNETLoader, Joy_caption_two, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, AIO_Preprocessor, VAELoader, DeepTranslatorTextNode, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader]
patterns: [lora]
missing: []
parameters: {"controlnet_strength": 0.6, "lora_name": "精致古装.safetensors", "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/反推提示词/Flux高清放大+TTP+Union 2.0控制_1948940603598544898.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Flux高清放大+TTP+Union 2.0控制_1948940603598544898.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `PreviewImage`
- `easy showAnything`
- `PreviewImage`
- `PreviewImage`
- `CFGGuider`
- `ConditioningCombine`
- `VAEEncode` ★核心
- `RandomNoise`
- `FluxGuidance`
- `TTP_Image_Tile_Batch`
- `ImageUpscaleWithModel`
- `ImageResize+`
- `ImageListToImageBatch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `TTP_Image_Assy`
- `ImpactImageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Note`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `Joy_caption_two_load`
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `ControlNetLoader`
- `StringFunction|pysssss`
- `ShowText|pysssss`
- `Reroute`
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Joy_caption_two`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `VAELoader`
- `DeepTranslatorTextNode`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `controlnet_strength` = `0.6`
- `lora_name` = `精致古装.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **76%**（41/54）

**有卡**：`CLIPTextEncode`、`SetUnionControlNetType`、`CFGGuider`、`ConditioningCombine`、`VAEEncode`、`RandomNoise`、`FluxGuidance`、`TTP_Image_Tile_Batch`、`ImageUpscaleWithModel`、`ImageResize+`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`TTP_Image_Assy`、`ImpactImageBatchToImageList`、`VAEDecodeTiled`、`KSamplerSelect`、`BasicScheduler`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`SaveImage`、`Joy_caption_two_load`、`DualCLIPLoader`、`LoraLoader`、`ControlNetLoader`、`StringFunction|pysssss`、`CLIPTextEncodeFlux`、`LoadImage`、`UNETLoader`、`Joy_caption_two`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`VAELoader`、`DeepTranslatorTextNode`、`UpscaleModelLoader`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、ControlNetApplyAdvanced、ControlNetLoader
