---
name: unknown_workflow_sampler_24
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.481667
common_nodes: [CR Text, Fast Groups Bypasser (rgthree), GenerateSRT, GetNode, IndexTTS2BaseNode, IndexTTS2CacheControlNode, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MergeAudioMW, RH_LLMAPI_NODE, ReplaceText, SRTToAudio, SaveAudio, SaveSRTFromString, SetNode, TrimAudioDuration, VoiceBridgeASRLoader, VoiceBridgeASRTranscribe, VoiceBridgeTTSLoader, VoiceClonePrompt, easy showAnything, easy string]
problems: []
missing: [VoiceBridgeAudioListMergerBySRT, VoiceBridgeSRTSplitter]
members: [音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json, 音频生成/音频生成/VoiceBridge workflow V2_2032102603814866945.json, 音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/AI翻译配音+字幕转音频+音频转字幕 多合一工作流 V3.1_2050059053363154946.json、音频生成/音频生成/VoiceBridge workflow V2_2032102603814866945.json、音频生成/音频生成/VoiceBridge 基础工作流 V2.1_2032633615116410882.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GenerateSRT`
- `GetNode`
- `IndexTTS2BaseNode`
- `IndexTTS2CacheControlNode`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MergeAudioMW`
- `RH_LLMAPI_NODE`
- `ReplaceText`
- `SRTToAudio`
- `SaveAudio`
- `SaveSRTFromString`
- `SetNode`
- `TrimAudioDuration`
- `VoiceBridgeASRLoader`
- `VoiceBridgeASRTranscribe`
- `VoiceBridgeTTSLoader`
- `VoiceClonePrompt`
- `easy showAnything`
- `easy string`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `FishS2VoiceCloneTTS` —— 1/3 个有
- `LongCatVoiceCloneTTS` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RunningHub_VoxCPM_Generate` —— 1/3 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `VoiceBridgeAudioListMergerBySRT` —— 1/3 个有
- `VoiceBridgeSRTSplitter` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：VoiceBridgeAudioListMergerBySRT、VoiceBridgeSRTSplitter
