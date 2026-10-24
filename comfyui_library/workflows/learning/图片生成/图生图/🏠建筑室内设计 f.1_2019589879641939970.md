---
key: 图片生成/图生图/🏠建筑室内设计 f.1_2019589879641939970.json
name: 🏠建筑室内设计 f.1_2019589879641939970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🏠建筑室内设计 f.1_2019589879641939970.json
hash: 67b9743217660172
coverage: 0.726619
learned_at: 2026-10-23 13:39:06
nodes: [AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, CheckpointLoaderSimple, UpscaleModelLoader, DualCLIPLoader, VAELoader, Note, StyleModelApply, AIO_Preprocessor, SetUnionControlNetType, PreviewImage, SetUnionControlNetType, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncodeFlux, FluxGuidance, ImageResizeKJ, VAEEncode, ImageUpscaleWithModel, easy imageScaleDownToSize, easy imageBatchToImageList, ImageScaleToTotalPixels, TTP_Image_Tile_Batch, NunchakuTextEncoderLoader, ConditioningZeroOut, CLIPTextEncode, ConditioningZeroOut, UpscaleModelLoader, TTP_Tile_image_size, KSampler, UltimateSDUpscale, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageListToBatch+, VAEDecodeTiled, TTP_Image_Assy, easy cleanGpuUsed, NunchakuFluxLoraLoader, Any Switch (rgthree), CLIPTextEncode, ControlNetLoader, ControlNetLoader, SetUnionControlNetType, PreviewImage, SetUnionControlNetType, LayerUtility: ImageScaleByAspectRatio V2, Reroute, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, AIO_Preprocessor, EmptyLatentImage, PreviewImage, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), PreviewImage, AIO_Preprocessor, KSampler, Mute / Bypass Relay (rgthree), PreviewImage, ControlNetApplySD3, ControlNetApplySD3, EmptyLatentImage, Any Switch (rgthree), AIO_Preprocessor, Note, Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), ControlNetApplySD3, PreviewImage, Mute / Bypass Relay (rgthree), ControlNetApplySD3, SetUnionControlNetType, AIO_Preprocessor, ControlNetApplySD3, Fast Groups Bypasser (rgthree), PrimitiveFloat, Seed (rgthree), PrimitiveFloat, KSampler, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), Any Switch (rgthree), LayerUtility: JoyCaptionBeta1, easy showAnything, StyleModelLoader, CLIPVisionLoader, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, ControlNetLoader, ControlNetLoader, ControlNetLoader, KSampler, KSampler, NunchakuFluxDiTLoader, easy int, easy int, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), VAEDecode, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), SaveImage, LoadImage, LoraLoader, UNETLoader, UNETLoader, VAELoader, DualCLIPLoader, LoraLoader]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "SD_XL/通用写实/juggernautXL_juggXIByRundiffusion.safetensors", "controlnet_strength": 0.6000000000000001, "denoise": 1, "height": 1024, "lora_name": "flux电影质感人物特写摄影_V3.0.safetensors", "sampler_name": "uni_pc", "scheduler": "sgm_uniform", "seed": 395707137808392, "steps": 40, "strength_clip": 0.6, "strength_model": 0.6600000000000001, "width": 1536}
---

# 图片生成/图生图/🏠建筑室内设计 f.1_2019589879641939970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🏠建筑室内设计 f.1_2019589879641939970.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（139 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CheckpointLoaderSimple` ★核心
- `UpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `Note`
- `StyleModelApply`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `PreviewImage`
- `SetUnionControlNetType`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `FluxGuidance`
- `ImageResizeKJ`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `easy imageScaleDownToSize`
- `easy imageBatchToImageList`
- `ImageScaleToTotalPixels`
- `TTP_Image_Tile_Batch`
- `NunchakuTextEncoderLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UpscaleModelLoader`
- `TTP_Tile_image_size`
- `KSampler` ★核心
- `UltimateSDUpscale`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageListToBatch+`
- `VAEDecodeTiled` ★核心
- `TTP_Image_Assy`
- `easy cleanGpuUsed`
- `NunchakuFluxLoraLoader` ★核心
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `PreviewImage`
- `SetUnionControlNetType`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `PreviewImage`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `Mute / Bypass Relay (rgthree)`
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `EmptyLatentImage` ★核心
- `Any Switch (rgthree)`
- `AIO_Preprocessor`
- `Note`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `Mute / Bypass Relay (rgthree)`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ControlNetApplySD3` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`
- `Seed (rgthree)`
- `PrimitiveFloat`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `LayerUtility: JoyCaptionBeta1`
- `easy showAnything`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `NunchakuFluxDiTLoader`
- `easy int`
- `easy int`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `LoraLoader` ★核心

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `checkpoint` = `SD_XL/通用写实/juggernautXL_juggXIByRundiffusion.safetensors`
- `seed` = `395707137808392`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.6000000000000001`
- `lora_name` = `flux电影质感人物特写摄影_V3.0.safetensors`
- `strength_model` = `0.6600000000000001`
- `strength_clip` = `0.6`

## 知识

覆盖率 **73%**（101/139）

**有卡**：`AIO_Preprocessor`、`CLIPTextEncode`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`UpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelApply`、`SetUnionControlNetType`、`CLIPVisionEncode`、`CLIPTextEncodeFlux`、`FluxGuidance`、`ImageResizeKJ`、`VAEEncode`、`ImageUpscaleWithModel`、`easy imageScaleDownToSize`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`NunchakuTextEncoderLoader`、`ConditioningZeroOut`、`TTP_Tile_image_size`、`KSampler`、`UltimateSDUpscale`、`ImageListToBatch+`、`VAEDecodeTiled`、`TTP_Image_Assy`、`NunchakuFluxLoraLoader`、`ControlNetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Relay (rgthree)`、`ControlNetApplySD3`、`Seed (rgthree)`、`LayerUtility: JoyCaptionBeta1`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`、`NunchakuFluxDiTLoader`、`easy int`、`VAEDecode`、`SaveImage`、`LoraLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
