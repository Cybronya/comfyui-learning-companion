---
key: 视频生成/图生视频/Wan2.2 最强效果Animate 视频人物姿态迁移V2升级版(保留原图背景）15S稳如老狗_1980606139123585025.json
name: Wan2.2 最强效果Animate 视频人物姿态迁移V2升级版(保留原图背景）15S稳如老狗_1980606139123585025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980606139123585025.json
hash: 3893232fc29f8611
coverage: 0.836735
learned_at: 2026-10-15 22:32:32
nodes: [GetNode, WanVideoDecode, WanVideoSetLoRAs, WanVideoBlockSwap, easy cleanGpuUsed, ImageConcatMulti, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionLoader, WanVideoTextEncodeCached, SimpleMath+, JWInteger, JWInteger, WanVideoClipVisionEncode, GetImageSizeAndCount, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoEncode, AudioSeparation, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, OnnxDetectionModelLoader, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, VHS_VideoInfo, WanVideoAnimateEmbeds, PoseAndFaceDetection, GetImageSizeAndCount, DrawViTPose, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, MultiTalkModelLoader, Fast Groups Bypasser (rgthree), CR Text, VHS_VideoCombine, VHS_VideoCombine, SetNode, GetNode, SetNode, LoadImage, GetNode, ImageConcatMulti, SetNode, GetNode, VHS_LoadVideo, ImpactInt, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 最强效果Animate 视频人物姿态迁移V2升级版(保留原图背景）15S稳如老狗_1980606139123585025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980606139123585025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `GetNode`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `OnnxDetectionModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `PoseAndFaceDetection`
- `GetImageSizeAndCount`
- `DrawViTPose`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `ImpactInt`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **84%**（41/49）

**有卡**：`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`ImageConcatMulti`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`SimpleMath+`、`JWInteger`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`OnnxDetectionModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`CR Text`、`VHS_VideoCombine`、`LoadImage`、`ImpactInt`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
