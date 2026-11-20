---
name: unknown_workflow_generic_615
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [CR Prompt Text, IndexTTSRun, LoadAudio, LoadVideo, RH_HeyGemNode, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/HeyGem数字人+INDEX TTS配音新版V3.0_1925857250173210626.json, 数字人/数字人/电商带货数字人带货（Heygem+IndexTTS工作流）_1958313041504976897.json, 视频生成/图生视频/HeyGem +IndexTTS_1925941668778823682.json, 视频生成/图生视频/SOTA数字人-HeyGem_1927266147043856386.json, 音频生成/音频生成/Heygem数字人带货对口型+IndexTTS文字生成音频对口型工作流_1947687290950795266.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_615

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/HeyGem数字人+INDEX TTS配音新版V3.0_1925857250173210626.json、数字人/数字人/电商带货数字人带货（Heygem+IndexTTS工作流）_1958313041504976897.json、视频生成/图生视频/HeyGem +IndexTTS_1925941668778823682.json、视频生成/图生视频/SOTA数字人-HeyGem_1927266147043856386.json、音频生成/音频生成/Heygem数字人带货对口型+IndexTTS文字生成音频对口型工作流_1947687290950795266.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Prompt Text`
- `IndexTTSRun`
- `LoadAudio`
- `LoadVideo`
- `RH_HeyGemNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `JWStringReplace` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
