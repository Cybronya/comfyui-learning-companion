---
name: unknown_workflow_generic_940
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7335
common_nodes: [IndexTTS2_ModelManager, LoadAudio, PrimitiveStringMultiline, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/Easy IndexTTS2情感克隆-高级语音工作流_2094736317346304002.json, 音频生成/音频生成/Easy IndexTTS2情感控制-情绪配音工作流_2094746968827457538.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_940

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Easy IndexTTS2情感克隆-高级语音工作流_2094736317346304002.json、音频生成/音频生成/Easy IndexTTS2情感控制-情绪配音工作流_2094746968827457538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `IndexTTS2_ModelManager`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2_Advanced` —— 1/2 个有
- `IndexTTS2_Emotion` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
