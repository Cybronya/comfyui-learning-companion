---
key: 视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json
name: AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json
hash: d12d7ad743eb0e54
coverage: 0.945946
learned_at: 2026-10-15 22:43:59
nodes: [WanVideoBlockSwap, AudioSeparation, FlashVSRNode, RH_GetAudioDuration, Float to Int, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, CLIPVisionLoader, easy anythingIndexSwitch, Apply Whisper, SoundFlow_TrimAudio, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, String Literal, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, VoxCPM_TTS, LoadAudio, Int, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
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
- `VHS_VideoCombine`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `CLIPVisionLoader`
- `easy anythingIndexSwitch`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `String Literal`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `VoxCPM_TTS`
- `LoadAudio`
- `Int`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`WanVideoBlockSwap`、`AudioSeparation`、`FlashVSRNode`、`RH_GetAudioDuration`、`Float to Int`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`SimpleMath+`、`WanVideoEasyCache`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`CLIPVisionLoader`、`easy anythingIndexSwitch`、`Apply Whisper`、`SoundFlow_TrimAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`String Literal`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VoxCPM_TTS`、`LoadAudio`、`Int`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
