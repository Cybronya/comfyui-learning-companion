---
name: unknown_workflow_generic_874
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8085
common_nodes: [CR Text, FishS2VoiceCloneTTS, LoadAudio, LoadWhisperModel_, SaveAudio, WhisperTranscribe_, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/万象AI+Fish Audio S2 TTS 批量英文配音_2038152218146246657.json, 音频生成/音频生成/最好的语音克隆 Fish Audio S2 TTS 全系工作流_2034524710632955906.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_874

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/万象AI+Fish Audio S2 TTS 批量英文配音_2038152218146246657.json、音频生成/音频生成/最好的语音克隆 Fish Audio S2 TTS 全系工作流_2034524710632955906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `FishS2VoiceCloneTTS`
- `LoadAudio`
- `LoadWhisperModel_`
- `SaveAudio`
- `WhisperTranscribe_`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FishS2MultiSpeakerTTS` —— 1/2 个有
- `FishS2TTS` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
