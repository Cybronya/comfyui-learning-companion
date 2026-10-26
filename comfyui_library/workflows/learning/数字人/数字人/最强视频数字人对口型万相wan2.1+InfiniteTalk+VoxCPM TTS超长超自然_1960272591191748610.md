---
key: 数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json
name: 最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json
hash: e6de168ad75fb0fc
coverage: 0.972222
learned_at: 2026-10-26 02:03:26
nodes: [GetNode, WanVideoDecode, WanVideoSampler, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, String Literal, INTConstant, INTConstant, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetImageSizeAndCount, GetImageRangeFromBatch, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LoadAudio, WanVideoBlockSwap, VHS_VideoCombine, RH_GetAudioDuration, Float to Int, SimpleMath+, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, Apply Whisper, SoundFlow_TrimAudio, AudioSeparation, easy anythingIndexSwitch, VoxCPM_TTS, WanVideoModelLoader, MultiTalkModelLoader]
patterns: []
missing: []
---

# 数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/最强视频数字人对口型万相wan2.1+InfiniteTalk+VoxCPM TTS超长超自然_1960272591191748610.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `String Literal`
- `INTConstant`
- `INTConstant`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadAudio`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `RH_GetAudioDuration`
- `Float to Int`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `AudioSeparation`
- `easy anythingIndexSwitch`
- `VoxCPM_TTS`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoDecode`、`WanVideoSampler`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`String Literal`、`INTConstant`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadAudio`、`WanVideoBlockSwap`、`RH_GetAudioDuration`、`Float to Int`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`Apply Whisper`、`SoundFlow_TrimAudio`、`AudioSeparation`、`easy anythingIndexSwitch`、`VoxCPM_TTS`、`WanVideoModelLoader`、`MultiTalkModelLoader`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
