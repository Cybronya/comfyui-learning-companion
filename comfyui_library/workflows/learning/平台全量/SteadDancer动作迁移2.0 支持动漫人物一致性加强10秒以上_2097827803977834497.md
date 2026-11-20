---
key: 平台全量/SteadDancer动作迁移2.0 支持动漫人物一致性加强10秒以上_2097827803977834497.json
name: SteadDancer动作迁移2.0 支持动漫人物一致性加强10秒以上_2097827803977834497
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SteadDancer动作迁移2.0 支持动漫人物一致性加强10秒以上_2097827803977834497.json
hash: 34a89e230759fbe7
coverage: 0.744444
learned_at: 2026-11-14 01:00:52
nodes: [ImageConcatMulti, WanVideoSetBlockSwap, SetNode, WanVideoEncode, GetNode, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, WanVideoAddSteadyDancerEmbeds, ImageConcatMulti, WanVideoSamplerSettings, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoDecode, WanVideoVAELoader, GetNode, WanVideoModelLoader, GetNode, GetNode, GetImageSizeAndCount, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, WanVideoSamplerFromSettings, PoseAndFaceDetection, WanVideoScheduler, GetNode, WanVideoClipVisionEncode, GetNode, WanVideoClipVisionEncode, VHS_LoadVideo, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoContextOptions, PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, Text, Int, MathExpression|pysssss, PreviewImage, RH_Sora2_I2V, LoadImage, VHS_VideoCombine, Int, Int, DF_Int_to_Float, SetNode, easy setNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, VHS_LoadVideo, LoadImage, GetImageRangeFromBatch, GetNode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SteadDancer动作迁移2.0 支持动漫人物一致性加强10秒以上_2097827803977834497.json

> 来源文件 `comfyui_library/workflows/平台全量/SteadDancer动作迁移2.0 支持动漫人物一致性加强10秒以上_2097827803977834497.json`

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
- `孤海注释`
- `孤海注释`
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

覆盖率 **74%**（67/90）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoSamplerSettings`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSamplerFromSettings`、`PoseAndFaceDetection`、`WanVideoScheduler`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoImageToVideoEncode`、`Text`、`Int`、`MathExpression|pysssss`、`RH_Sora2_I2V`、`LoadImage`、`VHS_VideoCombine`、`DF_Int_to_Float`、`easy setNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
