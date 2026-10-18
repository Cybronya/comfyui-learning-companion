---
key: 视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json
name: SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json
hash: 368973431acf76cd
coverage: 0.755556
learned_at: 2026-10-17 22:50:17
nodes: [ImageConcatMulti, WanVideoSetBlockSwap, SetNode, WanVideoEncode, GetNode, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, WanVideoSamplerSettings, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoDecode, WanVideoVAELoader, GetNode, WanVideoModelLoader, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSamplerFromSettings, PoseAndFaceDetection, WanVideoScheduler, GetNode, WanVideoClipVisionEncode, GetNode, WanVideoClipVisionEncode, VHS_LoadVideo, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, Text, Int, MathExpression|pysssss, PreviewImage, RH_Sora2_I2V, LoadImage, VHS_VideoCombine, Int, Int, DF_Int_to_Float, SetNode, easy setNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, VHS_LoadVideo, LoadImage, GetImageRangeFromBatch, GetNode, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/SteadDancer动作迁移2.0_支持动漫人物一致性加强10秒以上_2109098445825990657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `ImageResizeKJv2`
- `WanVideoAddSteadyDancerEmbeds`
- `ImageConcatMulti`
- `WanVideoSamplerSettings` ★核心
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSamplerFromSettings` ★核心
- `PoseAndFaceDetection`
- `WanVideoScheduler`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `Text`
- `Int`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_Sora2_I2V`
- `LoadImage`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `DF_Int_to_Float`
- `SetNode`
- `easy setNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **76%**（68/90）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSamplerFromSettings`、`PoseAndFaceDetection`、`WanVideoScheduler`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`Text`、`Int`、`MathExpression|pysssss`、`RH_Sora2_I2V`、`LoadImage`、`VHS_VideoCombine`、`DF_Int_to_Float`、`easy setNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
