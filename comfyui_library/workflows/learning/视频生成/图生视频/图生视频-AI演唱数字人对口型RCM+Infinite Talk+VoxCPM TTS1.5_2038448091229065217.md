---
key: 视频生成/图生视频/图生视频-AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2038448091229065217.json
name: 图生视频-AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2038448091229065217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038448091229065217.json
hash: 75e0a28216e461ca
coverage: 0.945946
learned_at: 2026-10-15 22:36:02
nodes: [WanVideoBlockSwap, AudioSeparation, FlashVSRNode, RH_GetAudioDuration, Float to Int, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, CLIPVisionLoader, easy anythingIndexSwitch, Apply Whisper, SoundFlow_TrimAudio, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, String Literal, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, VoxCPM_TTS, LoadAudio, Int, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频-AI演唱数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2038448091229065217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038448091229065217.json`

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
