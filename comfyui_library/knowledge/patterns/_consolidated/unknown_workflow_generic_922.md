---
name: unknown_workflow_generic_922
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.798
common_nodes: [IndexTTS2_MultiTalk, IndexTTS2_SpeakerEmotionConfig, LoadAudio, SaveAudio, Text Multiline]
problems: []
missing: []
members: [音频生成/音频生成/4人语音对话-IndexTTS2_1966718865164152834.json, 音频生成/音频生成/IndexTTS2四人语音克隆（可调节情绪）_1967092016792395778.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_922

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/4人语音对话-IndexTTS2_1966718865164152834.json、音频生成/音频生成/IndexTTS2四人语音克隆（可调节情绪）_1967092016792395778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `IndexTTS2_MultiTalk`
- `IndexTTS2_SpeakerEmotionConfig`
- `LoadAudio`
- `SaveAudio`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2_ModelManager` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
