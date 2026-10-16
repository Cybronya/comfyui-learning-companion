---
key: 视频生成/图生视频/数字人直播带货对口型RCM+Infinite Talk+VoxCPM TTS1.5_2027651848353615874.json
name: 数字人直播带货对口型RCM+Infinite Talk+VoxCPM TTS1.5_2027651848353615874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027651848353615874.json
hash: 3df1bd311b4a080d
coverage: 0.945946
learned_at: 2026-10-15 22:35:17
nodes: [WanVideoBlockSwap, AudioSeparation, FlashVSRNode, RH_GetAudioDuration, Float to Int, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, CLIPVisionLoader, easy anythingIndexSwitch, LoadAudio, Apply Whisper, SoundFlow_TrimAudio, LayerUtility: ImageScaleByAspectRatio V2, Int, WanVideoClipVisionEncode, PrimitiveStringMultiline, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, VoxCPM_TTS, LoadImage, String Literal]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人直播带货对口型RCM+Infinite Talk+VoxCPM TTS1.5_2027651848353615874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027651848353615874.json`

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
- `LoadAudio`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `WanVideoClipVisionEncode`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `VoxCPM_TTS`
- `LoadImage`
- `String Literal`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`WanVideoBlockSwap`、`AudioSeparation`、`FlashVSRNode`、`RH_GetAudioDuration`、`Float to Int`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`SimpleMath+`、`WanVideoEasyCache`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`CLIPVisionLoader`、`easy anythingIndexSwitch`、`LoadAudio`、`Apply Whisper`、`SoundFlow_TrimAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VoxCPM_TTS`、`LoadImage`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
