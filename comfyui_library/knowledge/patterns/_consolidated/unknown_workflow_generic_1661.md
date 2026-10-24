---
name: unknown_workflow_generic_1661
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [Apply Whisper, CR Prompt Text, LoadAudio, LongCatMultiSpeakerTTS, NormalizeAudioLoudness, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/LongCat-AudioDiT双人对话_2039911756067250178.json, 音频生成/音频生成/Longcat Audio DIT 三合一_2041930449106247682.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1661

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/LongCat-AudioDiT双人对话_2039911756067250178.json、音频生成/音频生成/Longcat Audio DIT 三合一_2041930449106247682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `CR Prompt Text`
- `LoadAudio`
- `LongCatMultiSpeakerTTS`
- `NormalizeAudioLoudness`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LongCatTTS` —— 1/2 个有
- `LongCatVoiceCloneTTS` —— 1/2 个有
- `SaveAudioOpus` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
