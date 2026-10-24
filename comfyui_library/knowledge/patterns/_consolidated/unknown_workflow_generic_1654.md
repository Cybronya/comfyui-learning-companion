---
name: unknown_workflow_generic_1654
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, LayerUtility: PurgeVRAM V2, LoadAudio, LoadVideo, RH_HeyGemNode, SaveVideo]
problems: []
missing: []
members: [音频生成/音频生成/Heygem数字人+IndexTTS文字对口型_1945485523890708482.json, 音频生成/音频生成/Heygem数字人带货对口型+IndexTTS文字生成音频对口型工作流_1947687290950795266.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1654

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Heygem数字人+IndexTTS文字对口型_1945485523890708482.json、音频生成/音频生成/Heygem数字人带货对口型+IndexTTS文字生成音频对口型工作流_1947687290950795266.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadVideo`
- `RH_HeyGemNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
