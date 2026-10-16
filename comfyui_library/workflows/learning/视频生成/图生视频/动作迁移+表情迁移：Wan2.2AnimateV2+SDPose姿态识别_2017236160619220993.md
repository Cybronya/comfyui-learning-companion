---
key: 视频生成/图生视频/动作迁移+表情迁移：Wan2.2AnimateV2+SDPose姿态识别_2017236160619220993.json
name: 动作迁移+表情迁移：Wan2.2AnimateV2+SDPose姿态识别_2017236160619220993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017236160619220993.json
hash: 14fe9e9a222d2a15
coverage: 0.650602
learned_at: 2026-10-15 22:34:46
nodes: [SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, WanVideoVAELoader, SetNode, GetNode, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, SetNode, VHS_VideoCombine, SDPoseOODLoader, SetNode, VHS_VideoCombine, YOLOModelLoader, VHS_VideoCombine, PoseAndFaceDetection, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoDecode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, CLIPVisionLoader, WanVideoSamplerv2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoContextOptions, WanVideoSamplerExtraArgs, AdaptiveWanVideoAnimateEmbeds, WanVideoTeaCache, Int, Int, LoadImage, Text, VHS_LoadVideo, ImageResizeKJv2, WanVideoLoraSelectMulti, SetNode, ImageScaleToTotalPixels, UNETLoader, LoraLoaderModelOnly, RandomNoise, CLIPLoader, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAEEncode, CFGGuider, KSamplerSelect, VAELoader, SamplerCustomAdvanced, EmptyFlux2LatentImage, Flux2Scheduler, VAEDecode, CLIPTextEncode, GetImageSize, Fast Groups Muter (rgthree), SaveImage, LoadImage, Int, SDPoseOODProcessor]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移+表情迁移：Wan2.2AnimateV2+SDPose姿态识别_2017236160619220993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017236160619220993.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SDPoseOODLoader`
- `SetNode`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoContextOptions`
- `WanVideoSamplerExtraArgs` ★核心
- `AdaptiveWanVideoAnimateEmbeds`
- `WanVideoTeaCache`
- `Int`
- `Int`
- `LoadImage`
- `Text`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `LoadImage`
- `Int`
- `SDPoseOODProcessor`

## 知识

覆盖率 **65%**（54/83）

**有卡**：`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`WanVideoSamplerExtraArgs`、`AdaptiveWanVideoAnimateEmbeds`、`WanVideoTeaCache`、`Int`、`LoadImage`、`Text`、`VHS_LoadVideo`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`ImageScaleToTotalPixels`、`UNETLoader`、`LoraLoaderModelOnly`、`RandomNoise`、`CLIPLoader`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`CFGGuider`、`KSamplerSelect`、`VAELoader`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`VAEDecode`、`CLIPTextEncode`、`GetImageSize`、`SaveImage`、`SDPoseOODProcessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
