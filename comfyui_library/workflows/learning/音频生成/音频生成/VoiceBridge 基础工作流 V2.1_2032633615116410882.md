---
key: 音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json
name: VoiceBridge 基础工作流 V2.1_2032633615116410882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json
hash: 91642d4434181413
coverage: 0.436364
learned_at: 2026-10-18 02:28:44
nodes: [easy showAnything, SetNode, SetNode, SetNode, GetNode, GetNode, CR Text, GenerateSRT, ReplaceText, SetNode, RH_LLMAPI_NODE, GetNode, Note, VoiceBridgeASRLoader, VoiceBridgeASRTranscribe, SetNode, SetNode, easy showAnything, Note, VoiceBridgeASRLoader, LoadAudio, SetNode, Fast Groups Bypasser (rgthree), TrimAudioDuration, easy showAnything, GetNode, SetNode, Note, easy string, Note, GetNode, SaveAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SetNode, SetNode, Note, GetNode, MergeAudioMW, SaveSRTFromString, VoiceBridgeTTSLoader, SRTToAudio, SaveAudio, VoiceBridgeASRTranscribe, VoiceBridgeASRTranscribe, LoadAudio, VoiceClonePrompt, Any Switch (rgthree), GetNode, GetNode, GetNode, IndexTTS2CacheControlNode, PrimitiveString, Any Switch (rgthree), IndexTTS2BaseNode]
patterns: []
missing: []
---

# 音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（55 个）：
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `GenerateSRT`
- `ReplaceText`
- `SetNode`
- `RH_LLMAPI_NODE`
- `GetNode`
- `Note`
- `VoiceBridgeASRLoader`
- `VoiceBridgeASRTranscribe`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `Note`
- `VoiceBridgeASRLoader`
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
- `GetNode`
- `SaveAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `MergeAudioMW`
- `SaveSRTFromString`
- `VoiceBridgeTTSLoader`
- `SRTToAudio`
- `SaveAudio`
- `VoiceBridgeASRTranscribe`
- `VoiceBridgeASRTranscribe`
- `LoadAudio`
- `VoiceClonePrompt`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `IndexTTS2CacheControlNode`
- `PrimitiveString`
- `Any Switch (rgthree)`
- `IndexTTS2BaseNode`

## 知识

覆盖率 **44%**（24/55）

**有卡**：`CR Text`、`GenerateSRT`、`ReplaceText`、`RH_LLMAPI_NODE`、`VoiceBridgeASRLoader`、`VoiceBridgeASRTranscribe`、`LoadAudio`、`TrimAudioDuration`、`easy string`、`SaveAudio`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`MergeAudioMW`、`SaveSRTFromString`、`VoiceBridgeTTSLoader`、`SRTToAudio`、`VoiceClonePrompt`、`IndexTTS2CacheControlNode`、`IndexTTS2BaseNode`

**用到的条目**：MelBandRoFormerSampler、VoiceClonePrompt、SaveAudio、SaveSRTFromString、LoadAudio、RH_LLMAPI_NODE、TrimAudioDuration、ReplaceText
