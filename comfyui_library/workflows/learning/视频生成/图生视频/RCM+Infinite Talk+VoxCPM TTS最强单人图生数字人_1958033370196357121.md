---
key: 视频生成/图生视频/RCM+Infinite Talk+VoxCPM TTS最强单人图生数字人_1958033370196357121.json
name: RCM+Infinite Talk+VoxCPM TTS最强单人图生数字人_1958033370196357121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/RCM+Infinite Talk+VoxCPM TTS最强单人图生数字人_1958033370196357121.json
hash: 13410f1583f0e24b
coverage: 0.973684
learned_at: 2026-10-15 22:31:20
nodes: [WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoEasyCache, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, MultiTalkWav2VecEmbeds, Float to Int, RH_GetAudioDuration, WanVideoDecode, LayerUtility: PurgeVRAM V2, CR Prompt Text, LoadImage, JWInteger, SimpleMath+, String Literal, WanVideoLoraSelect, WanVideoTextEncodeCached, easy anythingIndexSwitch, SoundFlow_TrimAudio, Apply Whisper, RHHiddenNodes, AudioSeparation, MultiTalkModelLoader, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, Wan22PromptSelector, LoadAudio, WanVideoSampler, VHS_VideoCombine, WanVideoModelLoader, easy anythingIndexSwitch, VoxCPM_TTS, WanVideoLoraSelect, WanVideoImageToVideoMultiTalk]
patterns: []
missing: []
---

# 视频生成/图生视频/RCM+Infinite Talk+VoxCPM TTS最强单人图生数字人_1958033370196357121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958033370196357121.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoEasyCache`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `MultiTalkWav2VecEmbeds`
- `Float to Int`
- `RH_GetAudioDuration`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `CR Prompt Text`
- `LoadImage`
- `JWInteger`
- `SimpleMath+`
- `String Literal`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `easy anythingIndexSwitch`
- `SoundFlow_TrimAudio`
- `Apply Whisper`
- `RHHiddenNodes`
- `AudioSeparation`
- `MultiTalkModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `Wan22PromptSelector`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `VoxCPM_TTS`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoMultiTalk`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoEasyCache`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`MultiTalkWav2VecEmbeds`、`Float to Int`、`RH_GetAudioDuration`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`CR Prompt Text`、`LoadImage`、`JWInteger`、`SimpleMath+`、`String Literal`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`easy anythingIndexSwitch`、`SoundFlow_TrimAudio`、`Apply Whisper`、`RHHiddenNodes`、`AudioSeparation`、`MultiTalkModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Wan22PromptSelector`、`LoadAudio`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoModelLoader`、`VoxCPM_TTS`、`WanVideoImageToVideoMultiTalk`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
