---
key: 平台全量/VoiceBridge V2 + Infinity Talk_2032109440257761282.json
name: VoiceBridge V2 + Infinity Talk_2032109440257761282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VoiceBridge V2 + Infinity Talk_2032109440257761282.json
hash: ff6015b64b37e4ae
coverage: 0.556818
learned_at: 2026-11-14 01:03:27
nodes: [easy showAnything, SetNode, SetNode, SetNode, GetNode, GenerateSRT, ReplaceText, SetNode, RH_LLMAPI_NODE, VoiceBridgeTTSLoader, GetNode, Note, VoiceBridgeASRLoader, VoiceBridgeASRTranscribe, SetNode, SetNode, easy showAnything, Note, LoadAudio, SetNode, Fast Groups Bypasser (rgthree), TrimAudioDuration, easy showAnything, GetNode, SetNode, Note, easy string, Note, SetNode, MelBandRoFormerModelLoader, GetNode, SaveSRTFromString, GetNode, IndexTTS2CacheControlNode, IndexTTS2BaseNode, Float to Int, SoundFlow_GetLength, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, Reroute, AudioCrop, Reroute, WanVideoVAELoader, Reroute, Reroute, Reroute, CLIPVisionLoader, Reroute, DownloadAndLoadWav2VecModel, Reroute, Reroute, SimpleMath+, AudioSeparation, WanVideoBlockSwap, Reroute, WanVideoImageToVideoMultiTalk, GetImageRangeFromBatch, WanVideoClipVisionEncode, WanVideoEncode, MultiTalkWav2VecEmbeds, WanVideoTextEncodeCached, JWStringMultiline, SetNode, SetNode, SetNode, GetNode, GetNode, SaveAudio, VHS_LoadVideo, GetNode, GetNode, MelBandRoFormerSampler, MergeAudioMW, SaveAudio, VoiceBridgeASRTranscribe, VoiceBridgeASRTranscribe, VoiceBridgeASRLoader, VoiceClonePrompt, SRTToAudio, CR Text, Note, Int, LayerUtility: ImageScaleByAspectRatio, VoiceBridgeUnloadModel]
patterns: []
missing: []
---

# 平台全量/VoiceBridge V2 + Infinity Talk_2032109440257761282.json

> 来源文件 `comfyui_library/workflows/平台全量/VoiceBridge V2 + Infinity Talk_2032109440257761282.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（88 个）：
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GenerateSRT`
- `ReplaceText`
- `SetNode`
- `RH_LLMAPI_NODE`
- `VoiceBridgeTTSLoader`
- `GetNode`
- `Note`
- `VoiceBridgeASRLoader`
- `VoiceBridgeASRTranscribe`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `Note`
- `LoadAudio`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `TrimAudioDuration`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `Note`
- `easy string`
- `Note`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `SaveSRTFromString`
- `GetNode`
- `IndexTTS2CacheControlNode`
- `IndexTTS2BaseNode`
- `Float to Int`
- `SoundFlow_GetLength`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `Reroute`
- `AudioCrop`
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPVisionLoader`
- `Reroute`
- `DownloadAndLoadWav2VecModel`
- `Reroute`
- `Reroute`
- `SimpleMath+`
- `AudioSeparation`
- `WanVideoBlockSwap`
- `Reroute`
- `WanVideoImageToVideoMultiTalk`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncodeCached`
- `JWStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveAudio`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `MergeAudioMW`
- `SaveAudio`
- `VoiceBridgeASRTranscribe`
- `VoiceBridgeASRTranscribe`
- `VoiceBridgeASRLoader`
- `VoiceClonePrompt`
- `SRTToAudio`
- `CR Text`
- `Note`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio`
- `VoiceBridgeUnloadModel`

## 知识

覆盖率 **56%**（49/88）

**有卡**：`GenerateSRT`、`ReplaceText`、`RH_LLMAPI_NODE`、`VoiceBridgeTTSLoader`、`VoiceBridgeASRLoader`、`VoiceBridgeASRTranscribe`、`LoadAudio`、`TrimAudioDuration`、`easy string`、`MelBandRoFormerModelLoader`、`SaveSRTFromString`、`IndexTTS2CacheControlNode`、`IndexTTS2BaseNode`、`Float to Int`、`SoundFlow_GetLength`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`AudioCrop`、`WanVideoVAELoader`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`SimpleMath+`、`AudioSeparation`、`WanVideoBlockSwap`、`WanVideoImageToVideoMultiTalk`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncodeCached`、`JWStringMultiline`、`SaveAudio`、`VHS_LoadVideo`、`MelBandRoFormerSampler`、`MergeAudioMW`、`VoiceClonePrompt`、`SRTToAudio`、`CR Text`、`Int`、`LayerUtility: ImageScaleByAspectRatio`、`VoiceBridgeUnloadModel`

**用到的条目**：MelBandRoFormerSampler、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
