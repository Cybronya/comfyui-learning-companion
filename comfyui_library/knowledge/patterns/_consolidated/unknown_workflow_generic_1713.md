---
name: unknown_workflow_generic_1713
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [LoadAudio, SaveAudio, easy downloadIndexTTSAndLoadModel, easy indexTTSEmotionVector, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [音频生成/音频生成/【精准控制声音情绪】IndexTTS2声音克隆【参考声音音色+参考声音情绪+文本】→【克隆声音】_2067141515532656642.json, 音频生成/音频生成/智造ai克隆音频_2079214947183185922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1713

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/【精准控制声音情绪】IndexTTS2声音克隆【参考声音音色+参考声音情绪+文本】→【克隆声音】_2067141515532656642.json、音频生成/音频生成/智造ai克隆音频_2079214947183185922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `SaveAudio`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSEmotionVector`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
