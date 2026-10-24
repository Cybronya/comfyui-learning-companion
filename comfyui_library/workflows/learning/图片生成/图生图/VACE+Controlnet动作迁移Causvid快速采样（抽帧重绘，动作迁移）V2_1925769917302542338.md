---
key: 图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json
name: VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json
hash: 00790b8ab623c453
coverage: 0.68323
learned_at: 2026-10-23 11:27:12
nodes: [LoadImage, PrimitiveInt, PrimitiveInt, ImageResizeKJ, Reroute, DualCLIPLoader, easy anythingIndexSwitch, DeepTranslatorTextNode, JoinStringMulti, easy anythingIndexSwitch, SetNode, RH_Captioner, JoinStringMulti, GetNode, Joy_caption_load, DeepTranslatorTextNode, ShowText|pysssss, easy anythingIndexSwitch, SetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, DWPreprocessor, DepthAnythingV2Preprocessor, AnyLineArtPreprocessor_aux, Grayscale Image (WLSH), GetNode, easy anythingIndexSwitch, Note, SetNode, PreviewImage, easy int, UNETLoader, ControlNetLoader, LongCLIPTextEncodeFlux, VAELoader, CLIPTextEncode, GetNode, GetNode, VAEDecode, SetNode, PreviewImage, GetNode, GetNode, ImageResize+, ImageUpscaleWithModel, TTP_Image_Tile_Batch, ImageResize+, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustomAdvanced, TTP_Tile_image_size, Joy_caption, Joy_caption, Joy_caption, LayerUtility: PurgeVRAM, JjkText, easy imageConcat, SetUnionControlNetType, SetUnionControlNetType, SetUnionControlNetType, SetUnionControlNetType, EmptyLatentImage, ConditioningZeroOut, FluxGuidance, SaveImage, PreviewImage, FluxGuidance, easy imageBatchToImageList, ShowText|pysssss, JjkText, Note, Note, VHS_LoadVideo, BasicGuider, GetNode, ImageResize+, SetNode, KSampler, ControlNetApplySD3, SetNode, UpscaleModelLoader, VAELoader, BasicScheduler, KSamplerSelect, RandomNoise, VAEEncode, GetNode, GetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, ImageResize+, easy imageConcat, SetNode, GetNode, GetNode, SetNode, VAEDecodeTiled, TTP_Image_Assy, Reroute, Image Comparer (rgthree), ImageResize+, GetNode, ImageResize+, easy imageChooser, ImageScaleToTotalPixels, SaveImage, LayerUtility: PurgeVRAM, SaveImage, Note, Note, WanVideoExperimentalArgs, Text Multiline, VHS_VideoCombine, RIFE VFI, ImageResizeKJ, Fast Groups Bypasser (rgthree), ImageConcatMulti, UpscaleModelLoader, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTeaCache, WanVideoTorchCompileSettings, WanVideoBlockSwap, Text Concatenate, Note, Note, GetNode, GetNode, SetNode, GetNode, GetNode, WanVideoVACEModelSelect, WanVideoModelLoader, VHS_VideoCombine, WanVideoVAELoader, WanVideoVACEEncode, WanVideoSampler, AIO_Preprocessor, VHS_LoadVideo, GetImageRangeFromBatch, ImageBlend, DWPreprocessor, RH_Captioner, ImageResizeKJ, LoadImage, ImageResizeKJ, WanVideoTextEncode, LoadWanVideoT5TextEncoder, VHS_VideoCombine, VHS_VideoCombine, ImageUpscaleWithModel, WanVideoDecode, ColorMatch, VHS_VideoCombine, WanVideoLoraSelect, Note]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 954321588843454, "steps": 30, "width": 864}
---

# 图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（161 个）：
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJ`
- `Reroute`
- `DualCLIPLoader`
- `easy anythingIndexSwitch`
- `DeepTranslatorTextNode`
- `JoinStringMulti`
- `easy anythingIndexSwitch`
- `SetNode`
- `RH_Captioner`
- `JoinStringMulti`
- `GetNode`
- `Joy_caption_load`
- `DeepTranslatorTextNode`
- `ShowText|pysssss`
- `easy anythingIndexSwitch`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `AnyLineArtPreprocessor_aux`
- `Grayscale Image (WLSH)`
- `GetNode`
- `easy anythingIndexSwitch`
- `Note`
- `SetNode`
- `PreviewImage`
- `easy int`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `LongCLIPTextEncodeFlux` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `TTP_Tile_image_size`
- `Joy_caption`
- `Joy_caption`
- `Joy_caption`
- `LayerUtility: PurgeVRAM`
- `JjkText`
- `easy imageConcat`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `SaveImage`
- `PreviewImage`
- `FluxGuidance`
- `easy imageBatchToImageList`
- `ShowText|pysssss`
- `JjkText`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `BasicGuider`
- `GetNode`
- `ImageResize+`
- `SetNode`
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `SetNode`
- `UpscaleModelLoader`
- `VAELoader`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `ImageResize+`
- `easy imageConcat`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `TTP_Image_Assy`
- `Reroute`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `GetNode`
- `ImageResize+`
- `easy imageChooser`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `Note`
- `Note`
- `WanVideoExperimentalArgs`
- `Text Multiline`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageResizeKJ`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `UpscaleModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Text Concatenate`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `AIO_Preprocessor`
- `VHS_LoadVideo`
- `GetImageRangeFromBatch`
- `ImageBlend`
- `DWPreprocessor`
- `RH_Captioner`
- `ImageResizeKJ`
- `LoadImage`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `WanVideoDecode`
- `ColorMatch`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `864`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `954321588843454`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **68%**（110/161）

**有卡**：`LoadImage`、`ImageResizeKJ`、`DualCLIPLoader`、`easy anythingIndexSwitch`、`DeepTranslatorTextNode`、`JoinStringMulti`、`RH_Captioner`、`Joy_caption_load`、`LayerUtility: PurgeVRAM`、`DWPreprocessor`、`DepthAnythingV2Preprocessor`、`AnyLineArtPreprocessor_aux`、`Grayscale Image (WLSH)`、`easy int`、`UNETLoader`、`ControlNetLoader`、`LongCLIPTextEncodeFlux`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`ImageResize+`、`ImageUpscaleWithModel`、`TTP_Image_Tile_Batch`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`TTP_Tile_image_size`、`Joy_caption`、`easy imageConcat`、`SetUnionControlNetType`、`EmptyLatentImage`、`ConditioningZeroOut`、`FluxGuidance`、`SaveImage`、`easy imageBatchToImageList`、`VHS_LoadVideo`、`BasicGuider`、`KSampler`、`ControlNetApplySD3`、`UpscaleModelLoader`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`VAEEncode`、`VAEDecodeTiled`、`TTP_Image_Assy`、`easy imageChooser`、`ImageScaleToTotalPixels`、`WanVideoExperimentalArgs`、`Text Multiline`、`VHS_VideoCombine`、`RIFE VFI`、`ImageConcatMulti`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Text Concatenate`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoSampler`、`AIO_Preprocessor`、`GetImageRangeFromBatch`、`ImageBlend`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ColorMatch`、`WanVideoLoraSelect`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
