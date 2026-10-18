---
key: 视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json
name: 【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json
hash: 5b0e8f5a47bdd2f2
coverage: 0.972222
learned_at: 2026-10-15 22:33:20
nodes: [GetNode, WanVideoDecode, WanVideoSampler, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, INTConstant, INTConstant, WanVideoModelLoader, CLIPVisionLoader, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetImageSizeAndCount, GetImageRangeFromBatch, ImageConcatMulti, VHS_VideoCombine, WanVideoBlockSwap, RH_GetAudioDuration, Float to Int, SimpleMath+, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, Apply Whisper, SoundFlow_TrimAudio, WanVideoVAELoader, VoxCPM_TTS, VHS_LoadVideo, easy anythingIndexSwitch, String Literal, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994362409961857025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `RH_GetAudioDuration`
- `Float to Int`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `WanVideoVAELoader`
- `VoxCPM_TTS`
- `VHS_LoadVideo`
- `easy anythingIndexSwitch`
- `String Literal`
- `LoadAudio`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoDecode`、`WanVideoSampler`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`INTConstant`、`WanVideoModelLoader`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`RH_GetAudioDuration`、`Float to Int`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`Apply Whisper`、`SoundFlow_TrimAudio`、`WanVideoVAELoader`、`VoxCPM_TTS`、`VHS_LoadVideo`、`easy anythingIndexSwitch`、`String Literal`、`LoadAudio`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
