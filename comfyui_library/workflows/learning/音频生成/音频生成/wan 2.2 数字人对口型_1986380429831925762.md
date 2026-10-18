---
key: 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json
name: wan 2.2 数字人对口型_1986380429831925762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json
hash: 418ba518168a8132
coverage: 0.967742
learned_at: 2026-10-18 01:46:57
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, RH_GetAudioDuration, CLIPVisionLoader, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, WanVideoModelLoader, Anything Everywhere, WanVideoVAELoader, SoundFlow_TrimAudio, AudioSeparation, VoxCPM_TTS, WanVideoSampler, WanVideoEncode, GetImageRangeFromBatch, WanVideoClipVisionEncode, GetImageSizeAndCount, ImageResizeKJv2, WanVideoImageToVideoMultiTalk, Apply Whisper, Float to Int, WanVideoTextEncodeCached, INTConstant, INTConstant, VHS_LoadVideo, String Literal, WanVideoDecode, VHS_VideoCombine, LoadAudio, SimpleMath+]
patterns: []
missing: []
---

# 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `RH_GetAudioDuration`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `WanVideoModelLoader`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `SoundFlow_TrimAudio`
- `AudioSeparation`
- `VoxCPM_TTS`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `WanVideoImageToVideoMultiTalk`
- `Apply Whisper`
- `Float to Int`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `String Literal`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadAudio`
- `SimpleMath+`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`RH_GetAudioDuration`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoModelLoader`、`WanVideoVAELoader`、`SoundFlow_TrimAudio`、`AudioSeparation`、`VoxCPM_TTS`、`WanVideoSampler`、`WanVideoEncode`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoImageToVideoMultiTalk`、`Apply Whisper`、`Float to Int`、`WanVideoTextEncodeCached`、`INTConstant`、`VHS_LoadVideo`、`String Literal`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadAudio`、`SimpleMath+`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
