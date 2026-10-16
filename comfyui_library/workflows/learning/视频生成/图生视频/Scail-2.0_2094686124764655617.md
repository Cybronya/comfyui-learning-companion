---
key: 视频生成/图生视频/Scail-2.0_2094686124764655617.json
name: Scail-2.0_2094686124764655617
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Scail-2.0_2094686124764655617.json
hash: ed55083078d6d42c
coverage: 0.707071
learned_at: 2026-10-17 00:02:35
nodes: [GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, SetNode, SetNode, PoseAndFaceDetection, PoseAndFaceDetection, SetNode, WanVideoVAELoader, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, GetNode, GetNode, SetNode, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoEncode, WanVideoSampler, WanVideoUni3C_embeds, LazySwitch1way, WanVideoClipVisionEncode, GetNode, SetNode, DrawViTPose, GetNode, YOLOModelLoader, BBoxYOLO, BBoxYOLO, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, WanVideoLoraSelectMulti, easy cleanGpuUsed, SDPoseKeypointExtractor, YOLOModelLoader, BodyRatioMapperSDPoseRender, WanVideoBlockSwap, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoContextOptions, WanVideoContextOptions, WanVideoContextOptions, WanVideoBlockSwap, LayerUtility: ColorImage V2, LazySwitch1way, easy compare, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, easy mathInt, easy float, SetNode, SetNode, SetNode, easy float, SetNode, easy float, SetNode, easy float, easy int, easy boolean, easy float, easy boolean, easy boolean, easy int, WanVideoUni3C_ControlnetLoader, SDPoseDrawKeypoints, WanVideoDecode, easy boolean, GetNode, easy imageSize, easy float, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, easy int, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, easy anythingIndexSwitch, easy float, LazySwitch2way, easy anythingIndexSwitch, easy int, easy int, WanVideoAnimateEmbeds, easy cleanGpuUsed, GetNode, WanVideoSampler, easy anythingIndexSwitch, easy int, AnyBooleanSwitch, easy anythingIndexSwitch, easy int, easy int, easy int, GetNode, GetNode, LazySwitch1way, PrimitiveBoolean, ZML_AnyTypeSwitchFiveBoolean, easy boolean, easy boolean, GetNode, ImageFromBatch, easy int, CompressImages, easy int, easy int, easy mathInt, easy int, easy int, easy compare, easy int, easy int, LazySwitch1way, easy int, ImpactSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch, ImpactSwitch, VHS_VideoCombine, VideoCombineNode, ImpactSwitch, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, BodyRatioMapperProportionTransfer, CR Text, CR Text, WanVideoTextEncodeCached, Note, VHS_LoadVideo, ImageScaleToTotalPixels, ImageResizeKJv2, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Scail-2.0_2094686124764655617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Scail-2.0_2094686124764655617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（198 个）：
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `BatchCount+`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `GetNode`
- `YOLOModelLoader`
- `BBoxYOLO`
- `BBoxYOLO`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `WanVideoLoraSelectMulti`
- `easy cleanGpuUsed`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `BodyRatioMapperSDPoseRender`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `easy anythingIndexSwitch`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `LayerUtility: ColorImage V2`
- `LazySwitch1way`
- `easy compare`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `easy float`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `easy int`
- `easy boolean`
- `easy float`
- `easy boolean`
- `easy boolean`
- `easy int`
- `WanVideoUni3C_ControlnetLoader`
- `SDPoseDrawKeypoints`
- `WanVideoDecode`
- `easy boolean`
- `GetNode`
- `easy imageSize`
- `easy float`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `easy anythingIndexSwitch`
- `easy float`
- `LazySwitch2way`
- `easy anythingIndexSwitch`
- `easy int`
- `easy int`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy anythingIndexSwitch`
- `easy int`
- `AnyBooleanSwitch`
- `easy anythingIndexSwitch`
- `easy int`
- `easy int`
- `easy int`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `PrimitiveBoolean`
- `ZML_AnyTypeSwitchFiveBoolean`
- `easy boolean`
- `easy boolean`
- `GetNode`
- `ImageFromBatch`
- `easy int`
- `CompressImages`
- `easy int`
- `easy int`
- `easy mathInt`
- `easy int`
- `easy int`
- `easy compare`
- `easy int`
- `easy int`
- `LazySwitch1way`
- `easy int`
- `ImpactSwitch`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VideoCombineNode`
- `ImpactSwitch`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `BodyRatioMapperProportionTransfer`
- `CR Text`
- `CR Text`
- `WanVideoTextEncodeCached`
- `Note`
- `VHS_LoadVideo`
- `ImageScaleToTotalPixels`
- `ImageResizeKJv2`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（140/198）

**有卡**：`CLIPVisionLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`WanVideoLoraSelectMulti`、`easy cleanGpuUsed`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoClipVisionEncode`、`DrawViTPose`、`YOLOModelLoader`、`BBoxYOLO`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`WanVideoBlockSwap`、`easy anythingIndexSwitch`、`WanVideoContextOptions`、`LayerUtility: ColorImage V2`、`easy compare`、`VHS_VideoInfo`、`easy float`、`easy int`、`easy boolean`、`WanVideoUni3C_ControlnetLoader`、`SDPoseDrawKeypoints`、`WanVideoDecode`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`LazySwitch2way`、`WanVideoAnimateEmbeds`、`AnyBooleanSwitch`、`PrimitiveBoolean`、`ZML_AnyTypeSwitchFiveBoolean`、`CompressImages`、`VHS_VideoCombine`、`VideoCombineNode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`BodyRatioMapperProportionTransfer`、`CR Text`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`ImageScaleToTotalPixels`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
