---
name: unknown_workflow_generic_1780
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6335
common_nodes: [AudioOmni_LoadModel, AudioOmni_TextToAudio, CR Prompt Text, Float, SaveAudioMP3]
problems: []
missing: [AudioOmni_LoadModel, AudioOmni_TextToAudio]
members: [音频生成/音频生成/Audio-Omni文生音效_2044266207385231361.json, 音频生成/音频生成/Audio-Omni文生音效_2044352972989140994.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1780

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Audio-Omni文生音效_2044266207385231361.json、音频生成/音频生成/Audio-Omni文生音效_2044352972989140994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioOmni_LoadModel`
- `AudioOmni_TextToAudio`
- `CR Prompt Text`
- `Float`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：AudioOmni_LoadModel、AudioOmni_TextToAudio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
