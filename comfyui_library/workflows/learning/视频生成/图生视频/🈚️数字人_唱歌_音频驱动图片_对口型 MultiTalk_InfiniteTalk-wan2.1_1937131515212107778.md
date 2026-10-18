---
key: 视频生成/图生视频/🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json
name: 🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json
hash: 6745025e2399a1e4
coverage: 0.419355
learned_at: 2026-10-15 22:30:28
nodes: [easy showAnything, GetNode, GetNode, PreviewAny, GetNode, GetNode, SetNode, GetNode, MultiTalkSilentEmbeds, MultiTalkWav2VecEmbeds, Audio Cut (mtb), GetNode, GetNode, ImageFromBatch+, GetNode, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, DownloadAndLoadWav2VecModel, GetImageSize, GetNode, GetNode, SetNode, WanVideoLoraSelect, WanVideoEncode, WanVideoUni3C_embeds, SetNode, AudioSeparation, GetNode, SetNode, easy showAnything, SetNode, GetNode, WanVideoContextOptions, SetNode, MultiTalkModelLoader, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, GetNode, SetNode, WanVideoTextEncodeSingle, GetNode, SetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, SetNode, GetNode, SetNode, easy seed, GetNode, Int, SetNode, SetNode, easy showAnything, easy showAnything, GetNode, GetNode, GetNode, GetNode, Int, GetNode, SetNode, SetNode, SetNode, ImageSmartSharpen+, LoadImage, LoadWanVideoClipTextEncoder, GetNode, VHS_LoadAudioUpload, Reroute, SimpleMath+, GetNode, SimpleMath+, GetNode, SetNode, FantasyPortraitModelLoader, GetNode, GetNode, GetNode, Any Switch (rgthree), GetNode, ImageResizeKJ, GetNode, WanVideoTorchCompileSettings, FantasyPortraitFaceDetector, VHS_VideoCombine, BboxVisualize, VHS_VideoCombine, WanVideoModelLoader, ImageResizeKJ, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, WanVideoAddFantasyPortrait, SetNode, GetNode, GetNode, LandmarksToImage, GetNode, Note, WanVideoDecode, VHS_LoadVideo, Text, GetNode, GetNode, VHS_LoadVideo, GetNode, Reroute, WanVideoSampler, Fast Groups Bypasser (rgthree), VHS_VideoCombine, SetNode, Reroute, GetNode, GetNode, VHS_LoadVideo, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937131515212107778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（124 个）：
- `easy showAnything`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `MultiTalkSilentEmbeds`
- `MultiTalkWav2VecEmbeds`
- `Audio Cut (mtb)`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `DownloadAndLoadWav2VecModel`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `AudioSeparation`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `WanVideoContextOptions`
- `SetNode`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `Int`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetNode`
- `VHS_LoadAudioUpload`
- `Reroute`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `SetNode`
- `FantasyPortraitModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `FantasyPortraitFaceDetector`
- `VHS_VideoCombine`
- `BboxVisualize`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `WanVideoAddFantasyPortrait`
- `SetNode`
- `GetNode`
- `GetNode`
- `LandmarksToImage`
- `GetNode`
- `Note`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `Text`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `Reroute`
- `WanVideoSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `SetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`

## 知识

覆盖率 **42%**（52/124）

**有卡**：`MultiTalkSilentEmbeds`、`MultiTalkWav2VecEmbeds`、`Audio Cut (mtb)`、`ImageFromBatch+`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`DownloadAndLoadWav2VecModel`、`GetImageSize`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`AudioSeparation`、`WanVideoContextOptions`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoUni3C_ControlnetLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`easy seed`、`Int`、`ImageSmartSharpen+`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`VHS_LoadAudioUpload`、`SimpleMath+`、`FantasyPortraitModelLoader`、`ImageResizeKJ`、`WanVideoTorchCompileSettings`、`FantasyPortraitFaceDetector`、`BboxVisualize`、`WanVideoModelLoader`、`WanVideoAddFantasyPortrait`、`LandmarksToImage`、`WanVideoDecode`、`VHS_LoadVideo`、`Text`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader
