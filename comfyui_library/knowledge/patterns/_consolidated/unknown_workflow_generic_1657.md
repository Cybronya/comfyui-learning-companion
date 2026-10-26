---
name: unknown_workflow_generic_1657
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [GetVideoComponents, IndexTTSNode, LoadVideo, RH_HeyGemNode, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/HeyGem数字人口播输入文本转语音声音克隆视频加音频生成ai数字人视频短评口播_2061109752800833538.json, 音频生成/音频生成/HeyGem数字人V2_1932991067656519682.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1657

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/HeyGem数字人口播输入文本转语音声音克隆视频加音频生成ai数字人视频短评口播_2061109752800833538.json、音频生成/音频生成/HeyGem数字人V2_1932991067656519682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `GetVideoComponents`
- `IndexTTSNode`
- `LoadVideo`
- `RH_HeyGemNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
