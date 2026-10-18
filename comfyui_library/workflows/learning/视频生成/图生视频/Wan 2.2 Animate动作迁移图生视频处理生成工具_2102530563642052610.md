---
key: 视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json
name: Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json
hash: 19b77a2a222c7d0a
coverage: 0.685
learned_at: 2026-10-17 02:29:26
nodes: [GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, LazySwitch1way, SetNode, SetNode, PoseAndFaceDetection, PoseAndFaceDetection, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, ImageFromBatch, ImageBatch, GetNode, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, GetNode, GetNode, Bool, Bool, easy anythingIndexSwitch, SetNode, WanVideoUni3C_ControlnetLoader, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoDecode, WanVideoSampler, WanVideoEncode, WanVideoSampler, easy cleanGpuUsed, WanVideoUni3C_embeds, LazySwitch1way, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, DrawViTPose, easy mathInt, GetNode, YOLOModelLoader, BBoxYOLO, ImageResizeKJv2, BBoxYOLO, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, SDPoseKeypointExtractor, WanVideoLoraSelectMulti, SDPoseDrawKeypoints, ImpactSwitch, Bool, easy mathInt, easy anythingIndexSwitch, ZML_AnyTypeSwitchFiveBoolean, VideoCombineNode, CompressImages, GetNode, easy cleanGpuUsed, SDPoseKeypointExtractor, YOLOModelLoader, easy int, BodyRatioMapperSDPoseRender, WanVideoBlockSwap, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoContextOptions, WanVideoContextOptions, WanVideoContextOptions, WanVideoBlockSwap, easy mathInt, LayerUtility: ColorImage V2, LazySwitch1way, easy compare, CR Text, CR Text, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, easy mathInt, easy anythingIndexSwitch, easy float, easy int, easy int, easy anythingIndexSwitch, easy int, SetNode, SetNode, SetNode, ImageResizeKJv2, easy imageSize, easy imageSize, LazySwitch2way, easy showAnything, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy float, easy float, ImpactSwitch, SetNode, SetNode, easy float, SetNode, easy float, SetNode, easy float, ImageScaleToTotalPixels, easy int, easy int, easy int, easy int, easy int, easy anythingIndexSwitch, ImageFromBatch, VHS_VideoCombine, easy int, easy compare, easy int, LazySwitch1way, easy showAnything, ImpactSwitch, easy int, easy boolean, easy boolean, BodyRatioMapperProportionTransfer, easy boolean, VHS_LoadVideo, LoadImage, easy boolean, SetNode, easy float, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（200 个）：
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
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
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
- `Bool`
- `Bool`
- `easy anythingIndexSwitch`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoUni3C_embeds`
- `LazySwitch1way`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `easy mathInt`
- `GetNode`
- `YOLOModelLoader`
- `BBoxYOLO`
- `ImageResizeKJv2`
- `BBoxYOLO`
- `easy anythingIndexSwitch`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `WanVideoLoraSelectMulti`
- `SDPoseDrawKeypoints`
- `ImpactSwitch`
- `Bool`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `ZML_AnyTypeSwitchFiveBoolean`
- `VideoCombineNode`
- `CompressImages`
- `GetNode`
- `easy cleanGpuUsed`
- `SDPoseKeypointExtractor`
- `YOLOModelLoader`
- `easy int`
- `BodyRatioMapperSDPoseRender`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `easy anythingIndexSwitch`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `easy mathInt`
- `LayerUtility: ColorImage V2`
- `LazySwitch1way`
- `easy compare`
- `CR Text`
- `CR Text`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `easy mathInt`
- `easy anythingIndexSwitch`
- `easy float`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `easy imageSize`
- `easy imageSize`
- `LazySwitch2way`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy float`
- `easy float`
- `ImpactSwitch`
- `SetNode`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `SetNode`
- `easy float`
- `ImageScaleToTotalPixels`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `easy int`
- `easy compare`
- `easy int`
- `LazySwitch1way`
- `easy showAnything`
- `ImpactSwitch`
- `easy int`
- `easy boolean`
- `easy boolean`
- `BodyRatioMapperProportionTransfer`
- `easy boolean`
- `VHS_LoadVideo`
- `LoadImage`
- `easy boolean`
- `SetNode`
- `easy float`
- `孤海注释`
- `孤海注释`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

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

覆盖率 **68%**（137/200）

**有卡**：`CLIPVisionLoader`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`ImageFromBatch`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`Bool`、`easy anythingIndexSwitch`、`WanVideoUni3C_ControlnetLoader`、`WanVideoLoraSelectMulti`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoClipVisionEncode`、`DrawViTPose`、`YOLOModelLoader`、`BBoxYOLO`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`ZML_AnyTypeSwitchFiveBoolean`、`VideoCombineNode`、`CompressImages`、`BodyRatioMapperSDPoseRender`、`WanVideoBlockSwap`、`WanVideoContextOptions`、`LayerUtility: ColorImage V2`、`easy compare`、`CR Text`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`easy float`、`easy imageSize`、`LazySwitch2way`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`VHS_VideoCombine`、`easy boolean`、`BodyRatioMapperProportionTransfer`、`VHS_LoadVideo`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
