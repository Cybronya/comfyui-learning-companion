---
key: 视频生成/图生视频/🈚️对口型+动作迁移+表情+运镜_翻唱 Multitalk_InfiniteTalk-wan2.1_1971491546132594689.json
name: 🈚️对口型+动作迁移+表情+运镜_翻唱 Multitalk_InfiniteTalk-wan2.1_1971491546132594689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971491546132594689.json
hash: 565da0ddb9377b16
coverage: 0.437908
learned_at: 2026-10-15 22:31:56
nodes: [easy showAnything, GetNode, GetNode, GetNode, PreviewAny, GetNode, GetNode, SetNode, GetNode, MultiTalkSilentEmbeds, MultiTalkWav2VecEmbeds, GetNode, Audio Cut (mtb), GetNode, GetNode, ImageFromBatch+, GetNode, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, FantasyPortraitFaceDetector, WanVideoDecode, DownloadAndLoadWav2VecModel, GetNode, GetImageSize, GetNode, GetNode, SetNode, FantasyPortraitModelLoader, WanVideoLoraSelect, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_embeds, SetNode, AudioSeparation, GetNode, GetNode, SetNode, easy showAnything, SetNode, GetNode, GetNode, WanVideoContextOptions, GetNode, SetNode, MultiTalkModelLoader, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, GetNode, SetNode, SetNode, WanVideoTextEncodeSingle, GetNode, SetNode, Fast Groups Bypasser (rgthree), OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSampler, Text, SetNode, ImageResizeKJ, PoseDetectionOneToAllAnimation, WanVideoUniAnimatePoseInput, SetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, SetNode, easy seed, GetNode, Int, SetNode, SetNode, ImageResizeKJ, easy showAnything, easy showAnything, GetNode, GetNode, GetNode, GetNode, Int, VHS_VideoCombine, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageSmartSharpen+, LoadImage, VHS_LoadVideo, WanVideoModelLoader, LoadWanVideoClipTextEncoder, GetNode, GetNode, VHS_LoadVideo, GetNode, GetNode, VHS_LoadVideo, Reroute, Reroute, VHS_LoadAudioUpload, Reroute, VHS_VideoCombine, Note, SimpleMath+, GetNode, SimpleMath+, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, GetNode, VHS_LoadVideo, Reroute, PreviewImage, PreviewImage, LoadLynxResampler, LynxEncodeFaceIP, easy imageRemBg, GetNode, WanVideoAddLynxEmbeds, WanVideoTextEncodeCached, LynxInsightFaceCrop, SetNode, WanVideoAddFantasyPortrait, ImpactControlBridge, easy cleanGpuUsed, Any Switch (rgthree), GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note, Reroute, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️对口型+动作迁移+表情+运镜_翻唱 Multitalk_InfiniteTalk-wan2.1_1971491546132594689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971491546132594689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（153 个）：
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `MultiTalkSilentEmbeds`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `Audio Cut (mtb)`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `FantasyPortraitFaceDetector`
- `WanVideoDecode`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `FantasyPortraitModelLoader`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `AudioSeparation`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `GetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `OnnxDetectionModelLoader`
- `WanVideoUni3C_ControlnetLoader`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `Text`
- `SetNode`
- `ImageResizeKJ`
- `PoseDetectionOneToAllAnimation`
- `WanVideoUniAnimatePoseInput`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `Int`
- `SetNode`
- `SetNode`
- `ImageResizeKJ`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `Reroute`
- `Reroute`
- `VHS_LoadAudioUpload`
- `Reroute`
- `VHS_VideoCombine`
- `Note`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `LoadLynxResampler` ★核心
- `LynxEncodeFaceIP`
- `easy imageRemBg`
- `GetNode`
- `WanVideoAddLynxEmbeds`
- `WanVideoTextEncodeCached`
- `LynxInsightFaceCrop`
- `SetNode`
- `WanVideoAddFantasyPortrait`
- `ImpactControlBridge`
- `easy cleanGpuUsed`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `Reroute`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **44%**（67/153）

**有卡**：`MultiTalkSilentEmbeds`、`MultiTalkWav2VecEmbeds`、`Audio Cut (mtb)`、`ImageFromBatch+`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`FantasyPortraitFaceDetector`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`GetImageSize`、`FantasyPortraitModelLoader`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`AudioSeparation`、`WanVideoContextOptions`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSampler`、`Text`、`ImageResizeKJ`、`PoseDetectionOneToAllAnimation`、`WanVideoUniAnimatePoseInput`、`easy cleanGpuUsed`、`easy seed`、`Int`、`ImageSmartSharpen+`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`VHS_LoadAudioUpload`、`SimpleMath+`、`LoadLynxResampler`、`LynxEncodeFaceIP`、`easy imageRemBg`、`WanVideoAddLynxEmbeds`、`WanVideoTextEncodeCached`、`LynxInsightFaceCrop`、`WanVideoAddFantasyPortrait`、`ImpactControlBridge`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadLynxResampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode
