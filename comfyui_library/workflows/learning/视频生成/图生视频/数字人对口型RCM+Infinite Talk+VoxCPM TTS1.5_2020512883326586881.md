---
key: 视频生成/图生视频/数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2020512883326586881.json
name: 数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2020512883326586881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2020512883326586881.json
hash: fb2a18c3758ba1ad
coverage: 0.945946
learned_at: 2026-10-15 22:35:06
nodes: [FlashVSRNode, RH_GetAudioDuration, SimpleMath+, Apply Whisper, SoundFlow_TrimAudio, VHS_VideoCombine, LoadImage, Int, LoadAudio, String Literal, easy anythingIndexSwitch, PrimitiveStringMultiline, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoEasyCache, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, WanVideoDecode, AudioSeparation, VoxCPM_TTS, Float to Int, WanVideoImageToVideoMultiTalk, MultiTalkWav2VecEmbeds, MultiTalkModelLoader, DownloadAndLoadWav2VecModel, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2020512883326586881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020512883326586881.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `FlashVSRNode`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `VHS_VideoCombine`
- `LoadImage`
- `Int`
- `LoadAudio`
- `String Literal`
- `easy anythingIndexSwitch`
- `PrimitiveStringMultiline`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `AudioSeparation`
- `VoxCPM_TTS`
- `Float to Int`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkWav2VecEmbeds`
- `MultiTalkModelLoader`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`FlashVSRNode`、`RH_GetAudioDuration`、`SimpleMath+`、`Apply Whisper`、`SoundFlow_TrimAudio`、`VHS_VideoCombine`、`LoadImage`、`Int`、`LoadAudio`、`String Literal`、`easy anythingIndexSwitch`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`LayerUtility: PurgeVRAM V2`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`AudioSeparation`、`VoxCPM_TTS`、`Float to Int`、`WanVideoImageToVideoMultiTalk`、`MultiTalkWav2VecEmbeds`、`MultiTalkModelLoader`、`DownloadAndLoadWav2VecModel`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
