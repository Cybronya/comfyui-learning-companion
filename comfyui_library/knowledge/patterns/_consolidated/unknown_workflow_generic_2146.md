---
name: unknown_workflow_generic_2146
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CR Prompt Text, LoadAudio, SaveAudio, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Pronunciation]
problems: []
missing: []
members: [音频生成/音频生成/SCAI创意分享 _ indextts2.5语音克隆 情感控制_2093694902956814338.json, 音频生成/音频生成/声音克隆多音字版加情绪控制版IndexTTS2.5多音字语音克隆(中文版)_2089989930364784641.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_2146

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/SCAI创意分享 _ indextts2.5语音克隆 情感控制_2093694902956814338.json、音频生成/音频生成/声音克隆多音字版加情绪控制版IndexTTS2.5多音字语音克隆(中文版)_2089989930364784641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LoadAudio`
- `SaveAudio`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Pronunciation`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SaveAudioAdvanced` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
