---
name: unknown_workflow_generic_950
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8635
common_nodes: [CR Prompt Text, IndexTTSRun, LoadAudio, LoadVideo, RH_HeyGemNode, SaveVideo]
problems: []
missing: []
members: [音频生成/音频生成/HeyGem数字人+语音克隆_1925738543635992577.json, 音频生成/音频生成/HeyGem数字人+语音克隆（极速生成）_1926023691921231874.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_950

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/HeyGem数字人+语音克隆_1925738543635992577.json、音频生成/音频生成/HeyGem数字人+语音克隆（极速生成）_1926023691921231874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `IndexTTSRun`
- `LoadAudio`
- `LoadVideo`
- `RH_HeyGemNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 1/2 个有
- `SaveAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
