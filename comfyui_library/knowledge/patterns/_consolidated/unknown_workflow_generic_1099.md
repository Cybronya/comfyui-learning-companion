---
name: unknown_workflow_generic_1099
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CR Prompt Text, IndexTTS2Run, LoadAudio, LoadVideo, RH_HeyGemNode, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/Heygem数字人+IndexTTS文字对口型_2019828616909037570.json, 数字人/数字人/英文对口型_2032779537045524482.json, 音频生成/音频生成/Heygem数字人+IndexTTS文字对口型_1945485523890708482.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1099

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Heygem数字人+IndexTTS文字对口型_2019828616909037570.json、数字人/数字人/英文对口型_2032779537045524482.json、音频生成/音频生成/Heygem数字人+IndexTTS文字对口型_1945485523890708482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `IndexTTS2Run`
- `LoadAudio`
- `LoadVideo`
- `RH_HeyGemNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SaveAudio` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
