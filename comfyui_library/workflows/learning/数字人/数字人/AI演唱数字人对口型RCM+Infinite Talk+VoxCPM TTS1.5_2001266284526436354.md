---
key: 数字人/数字人/AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2001266284526436354.json
name: AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2001266284526436354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2001266284526436354.json
hash: 40d7dcb91d029243
coverage: 0.947368
learned_at: 2026-10-26 01:53:44
nodes: [WanVideoBlockSwap, AudioSeparation, FlashVSRNode, RH_GetAudioDuration, Float to Int, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, WanVideoEasyCache, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, CLIPVisionLoader, Apply Whisper, SoundFlow_TrimAudio, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, VoxCPM_TTS, Int, LoadAudio, LoadImage, LoadImage, VHS_VideoCombine, easy anythingIndexSwitch, String Literal, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2001266284526436354.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2001266284526436354.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoBlockSwap`
- `AudioSeparation`
- `FlashVSRNode`
- `RH_GetAudioDuration`
- `Float to Int`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SimpleMath+`
- `WanVideoEasyCache`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `CLIPVisionLoader`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `VoxCPM_TTS`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `String Literal`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`WanVideoBlockSwap`、`AudioSeparation`、`FlashVSRNode`、`RH_GetAudioDuration`、`Float to Int`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`SimpleMath+`、`WanVideoEasyCache`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`CLIPVisionLoader`、`Apply Whisper`、`SoundFlow_TrimAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VoxCPM_TTS`、`Int`、`LoadAudio`、`LoadImage`、`easy anythingIndexSwitch`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
