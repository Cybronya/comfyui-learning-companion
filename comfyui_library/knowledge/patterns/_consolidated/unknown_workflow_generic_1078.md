---
name: unknown_workflow_generic_1078
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.622333
common_nodes: [AudioOmni_LoadModel, CR Prompt Text, JWInteger, SaveAudioMP3]
problems: []
missing: [AudioOmni_LoadModel, AudioOmni_TextToAudio, AudioOmni_TextToSpeech]
members: [音频生成/音频生成/Audio-Omni文生纯音乐_2044266571333378050.json, 音频生成/音频生成/Audio-Omni文生语音TTS_2044270079424073729.json, 音频生成/音频生成/Audio-Omni纯音乐生成_2044351098529521665.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1078

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Audio-Omni文生纯音乐_2044266571333378050.json、音频生成/音频生成/Audio-Omni文生语音TTS_2044270079424073729.json、音频生成/音频生成/Audio-Omni纯音乐生成_2044351098529521665.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioOmni_LoadModel`
- `CR Prompt Text`
- `JWInteger`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `AudioOmni_TextToAudio` —— 2/3 个有
- `AudioOmni_TextToSpeech` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：AudioOmni_LoadModel、AudioOmni_TextToAudio、AudioOmni_TextToSpeech
