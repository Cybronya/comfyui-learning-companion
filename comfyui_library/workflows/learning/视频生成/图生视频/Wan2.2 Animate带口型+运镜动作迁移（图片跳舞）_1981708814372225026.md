---
key: 视频生成/图生视频/Wan2.2 Animate带口型+运镜动作迁移（图片跳舞）_1981708814372225026.json
name: Wan2.2 Animate带口型+运镜动作迁移（图片跳舞）_1981708814372225026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate带口型+运镜动作迁移（图片跳舞）_1981708814372225026.json
hash: 497a5fd44d3fbc1c
coverage: 0.811321
learned_at: 2026-10-15 22:32:38
nodes: [PixelPerfectResolution, GetNode, ImageCropByMaskAndResize, SimpleMath+, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetLoRAs, VHS_VideoInfo, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoDecode, WanVideoAnimateEmbeds, GetNode, ImageConcatMulti, GetImageSizeAndCount, ImageResizeKJv2, WanVideoEncode, WanVideoUni3C_ControlnetLoader, MultiTalkModelLoader, AudioSeparation, DownloadAndLoadWav2VecModel, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, FaceMaskFromPoseKeypoints, ImageResizeKJv2, GetNode, SetNode, easy cleanGpuUsed, GetNode, SetNode, WanVideoUni3C_embeds, MultiTalkWav2VecEmbeds, ImpactInt, JWInteger, JWInteger, WanVideoModelLoader, WanVideoTextEncodeCached, CR Text, VHS_LoadVideo, LoadAudio, ImpactSwitch, SimpleCondition+, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, WanVideoSampler, RHHiddenNodes, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate带口型+运镜动作迁移（图片跳舞）_1981708814372225026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981708814372225026.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（53 个）：
- `PixelPerfectResolution`
- `GetNode`
- `ImageCropByMaskAndResize`
- `SimpleMath+`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `VHS_VideoInfo`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `MultiTalkModelLoader`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `WanVideoUni3C_embeds`
- `MultiTalkWav2VecEmbeds`
- `ImpactInt`
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `CR Text`
- `VHS_LoadVideo`
- `LoadAudio`
- `ImpactSwitch`
- `SimpleCondition+`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`SimpleMath+`、`LayerUtility: PurgeVRAM V2`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`VHS_VideoInfo`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`MultiTalkModelLoader`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`VHS_VideoCombine`、`FaceMaskFromPoseKeypoints`、`easy cleanGpuUsed`、`WanVideoUni3C_embeds`、`MultiTalkWav2VecEmbeds`、`ImpactInt`、`JWInteger`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`CR Text`、`VHS_LoadVideo`、`LoadAudio`、`SimpleCondition+`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
