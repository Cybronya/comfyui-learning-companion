---
key: 视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json
name: AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json
hash: d12d7ad743eb0e54
coverage: 0.756757
learned_at: 2026-10-11 03:48:33
nodes: [WanVideoBlockSwap, AudioSeparation, FlashVSRNode, RH_GetAudioDuration, Float to Int, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, SimpleMath+, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, CLIPVisionLoader, easy anythingIndexSwitch, Apply Whisper, SoundFlow_TrimAudio, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, String Literal, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, VoxCPM_TTS, LoadAudio, Int, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: [Apply Whisper, Float to Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, SimpleMath+, String Literal, easy anythingIndexSwitch]
discoveries: [次要节点 `Apply Whisper` 知识库中没有该节点类型的任何知识, 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识]
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

覆盖率 **76%**（28/37）

**有卡**：`WanVideoBlockSwap`、`AudioSeparation`、`FlashVSRNode`、`RH_GetAudioDuration`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoEasyCache`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`CLIPVisionLoader`、`SoundFlow_TrimAudio`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VoxCPM_TTS`、`LoadAudio`、`Int`、`LoadImage`

**缺卡**（7）：`Apply Whisper`、`Float to Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`String Literal`、`easy anythingIndexSwitch`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader

## 学习发现

- 次要节点 `Apply Whisper` 知识库中没有该节点类型的任何知识
- 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
