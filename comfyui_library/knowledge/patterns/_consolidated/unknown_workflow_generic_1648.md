---
name: unknown_workflow_generic_1648
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [CR Text, FishS2MultiSpeakerTTS, LazySwitch1way, LoadAudio, PreviewAny, RH_LLMAPI_NODE, SaveAudio, WhisperSTT, easy boolean, ttN concat]
problems: []
missing: []
members: [音频生成/音频生成/FishAudioS2-多人声音克隆【small-JJ小健健】_2040976378308337665.json, 音频生成/音频生成/声音克隆-FishAudioS2-单人_双人【small-JJ小健健】_2040287687734726658.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1648

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/FishAudioS2-多人声音克隆【small-JJ小健健】_2040976378308337665.json、音频生成/音频生成/声音克隆-FishAudioS2-单人_双人【small-JJ小健健】_2040287687734726658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `FishS2MultiSpeakerTTS`
- `LazySwitch1way`
- `LoadAudio`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `SaveAudio`
- `WhisperSTT`
- `easy boolean`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `FishS2VoiceCloneTTS` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
