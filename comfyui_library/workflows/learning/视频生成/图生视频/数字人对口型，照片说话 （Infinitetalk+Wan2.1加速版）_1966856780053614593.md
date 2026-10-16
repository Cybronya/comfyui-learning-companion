---
key: 视频生成/图生视频/数字人对口型，照片说话 （Infinitetalk+Wan2.1加速版）_1966856780053614593.json
name: 数字人对口型，照片说话 （Infinitetalk+Wan2.1加速版）_1966856780053614593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966856780053614593.json
hash: ea78bf04d9f640fa
coverage: 0.780488
learned_at: 2026-10-15 22:31:39
nodes: [WanVideoBlockSwap, WanVideoVAELoader, ImageResizeKJv2, WanVideoLoraSelect, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, SaveAudio, WanVideoImageToVideoMultiTalk, GetNode, GetNode, AudioSeparation, ToInt, SimpleMath+, easy showAnything, RH_GetAudioDuration, WanVideoSampler, easy cleanGpuUsed, WanVideoTextEncode, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, WanVideoModelLoader, AudioCrop, LoadAudio, CLIPVisionLoader, MultiTalkWav2VecEmbeds, easy showAnything, CM_IntToFloat, WanVideoDecode, PreviewImage, WanVideoClipVisionEncode, Anything Everywhere, LoadImage, Int, Note, INTConstant, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SaveAudio, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人对口型，照片说话 （Infinitetalk+Wan2.1加速版）_1966856780053614593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966856780053614593.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `SaveAudio`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `GetNode`
- `AudioSeparation`
- `ToInt`
- `SimpleMath+`
- `easy showAnything`
- `RH_GetAudioDuration`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `AudioCrop`
- `LoadAudio`
- `CLIPVisionLoader`
- `MultiTalkWav2VecEmbeds`
- `easy showAnything`
- `CM_IntToFloat`
- `WanVideoDecode`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `Anything Everywhere`
- `LoadImage`
- `Int`
- `Note`
- `INTConstant`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SaveAudio`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **78%**（32/41）

**有卡**：`WanVideoBlockSwap`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`SaveAudio`、`WanVideoImageToVideoMultiTalk`、`AudioSeparation`、`ToInt`、`SimpleMath+`、`RH_GetAudioDuration`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoTextEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`AudioCrop`、`LoadAudio`、`CLIPVisionLoader`、`MultiTalkWav2VecEmbeds`、`CM_IntToFloat`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`LoadImage`、`Int`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
