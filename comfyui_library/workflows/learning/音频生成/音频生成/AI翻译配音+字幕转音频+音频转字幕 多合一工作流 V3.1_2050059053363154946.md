---
key: 音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json
name: AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json
hash: 92aa7f0a965a85a0
coverage: 0.529412
learned_at: 2026-10-18 03:04:47
nodes: [easy showAnything, SetNode, SetNode, SetNode, GetNode, GetNode, ReplaceText, SetNode, GetNode, VoiceBridgeASRLoader, VoiceBridgeASRTranscribe, SetNode, SetNode, easy showAnything, VoiceBridgeASRLoader, SetNode, TrimAudioDuration, easy showAnything, GetNode, SetNode, Note, GetNode, SaveAudio, MelBandRoFormerModelLoader, SetNode, SetNode, GetNode, MergeAudioMW, SaveSRTFromString, VoiceBridgeASRTranscribe, VoiceBridgeASRTranscribe, VoiceClonePrompt, Any Switch (rgthree), GetNode, GetNode, IndexTTS2CacheControlNode, Any Switch (rgthree), SRTToAudio, VoiceBridgeTTSLoader, GenerateSRT, CR Text, easy string, Note, Note, VoiceBridgeAudioListMergerBySRT, VoiceBridgeAudioListMergerBySRT, Note, RunningHub_VoxCPM_LoadModel, VoiceBridgeSRTSplitter, SaveAudioMP3, RunningHub_VoxCPM_Generate, SaveAudioMP3, VoiceBridgeAudioListMergerBySRT, FishS2VoiceCloneTTS, easy showAnything, SaveSRTFromString, easy showAnything, SaveSRTFromString, easy showAnything, SaveSRTFromString, MelBandRoFormerSampler, MelBandRoFormerSampler, VoiceBridgeASRLoader, VoiceBridgeASRTranscribe, GenerateSRT, easy showAnything, MelBandRoFormerModelLoader, LoadAudio, MelBandRoFormerModelLoader, SaveAudioMP3, SaveAudioMP3, MelBandRoFormerSampler, SaveAudioMP3, VoiceBridgeSRTSplitter, LoadAudio, LongCatVoiceCloneTTS, PrimitiveStringMultiline, LoadAudio, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadAudio, VoiceBridgeSRTSplitter, PrimitiveStringMultiline, LoadAudio, LoadAudio, Note, LoadAudio, SaveAudio, PrimitiveStringMultiline, LoadAudio, VoiceBridgeTTSLoader, VoiceClonePrompt, SRTToAudio, SaveAudio, SaveSRTFromString, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, GetNode, IndexTTS2BaseNode, RH_LLMAPI_NODE]
patterns: []
missing: [VoiceBridgeAudioListMergerBySRT, VoiceBridgeAudioListMergerBySRT, VoiceBridgeAudioListMergerBySRT, VoiceBridgeSRTSplitter, VoiceBridgeSRTSplitter, VoiceBridgeSRTSplitter]
discoveries: [次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识, 次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识, 次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识, 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识, 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识, 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识]
---

# 音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（102 个）：
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ReplaceText`
- `SetNode`
- `GetNode`
- `VoiceBridgeASRLoader`
- `VoiceBridgeASRTranscribe`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `VoiceBridgeASRLoader`
- `SetNode`
- `TrimAudioDuration`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SaveAudio`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `MergeAudioMW`
- `SaveSRTFromString`
- `VoiceBridgeASRTranscribe`
- `VoiceBridgeASRTranscribe`
- `VoiceClonePrompt`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `IndexTTS2CacheControlNode`
- `Any Switch (rgthree)`
- `SRTToAudio`
- `VoiceBridgeTTSLoader`
- `GenerateSRT`
- `CR Text`
- `easy string`
- `Note`
- `Note`
- `VoiceBridgeAudioListMergerBySRT`
- `VoiceBridgeAudioListMergerBySRT`
- `Note`
- `RunningHub_VoxCPM_LoadModel`
- `VoiceBridgeSRTSplitter`
- `SaveAudioMP3`
- `RunningHub_VoxCPM_Generate`
- `SaveAudioMP3`
- `VoiceBridgeAudioListMergerBySRT`
- `FishS2VoiceCloneTTS`
- `easy showAnything`
- `SaveSRTFromString`
- `easy showAnything`
- `SaveSRTFromString`
- `easy showAnything`
- `SaveSRTFromString`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `VoiceBridgeASRLoader`
- `VoiceBridgeASRTranscribe`
- `GenerateSRT`
- `easy showAnything`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `SaveAudioMP3`
- `SaveAudioMP3`
- `MelBandRoFormerSampler` ★核心
- `SaveAudioMP3`
- `VoiceBridgeSRTSplitter`
- `LoadAudio`
- `LongCatVoiceCloneTTS`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `VoiceBridgeSRTSplitter`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoadAudio`
- `Note`
- `LoadAudio`
- `SaveAudio`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `VoiceBridgeTTSLoader`
- `VoiceClonePrompt`
- `SRTToAudio`
- `SaveAudio`
- `SaveSRTFromString`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `IndexTTS2BaseNode`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **53%**（54/102）

**有卡**：`ReplaceText`、`VoiceBridgeASRLoader`、`VoiceBridgeASRTranscribe`、`TrimAudioDuration`、`SaveAudio`、`MelBandRoFormerModelLoader`、`MergeAudioMW`、`SaveSRTFromString`、`VoiceClonePrompt`、`IndexTTS2CacheControlNode`、`SRTToAudio`、`VoiceBridgeTTSLoader`、`GenerateSRT`、`CR Text`、`easy string`、`RunningHub_VoxCPM_LoadModel`、`SaveAudioMP3`、`RunningHub_VoxCPM_Generate`、`FishS2VoiceCloneTTS`、`MelBandRoFormerSampler`、`LoadAudio`、`LongCatVoiceCloneTTS`、`IndexTTS2BaseNode`、`RH_LLMAPI_NODE`

**缺卡**（6）：`VoiceBridgeAudioListMergerBySRT`、`VoiceBridgeAudioListMergerBySRT`、`VoiceBridgeAudioListMergerBySRT`、`VoiceBridgeSRTSplitter`、`VoiceBridgeSRTSplitter`、`VoiceBridgeSRTSplitter`

**用到的条目**：MelBandRoFormerSampler、VoiceClonePrompt、SaveAudio、SaveAudioMP3、SaveSRTFromString、LoadAudio、RH_LLMAPI_NODE、TrimAudioDuration

## 学习发现

- 次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识
- 次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识
- 次要节点 `VoiceBridgeAudioListMergerBySRT` 知识库中没有该节点类型的任何知识
- 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识
- 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识
- 次要节点 `VoiceBridgeSRTSplitter` 知识库中没有该节点类型的任何知识
