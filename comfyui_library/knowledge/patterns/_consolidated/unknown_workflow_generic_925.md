---
name: unknown_workflow_generic_925
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.874333
common_nodes: [LoadImage, RHLLMChatNode, SaveImage, ShowText|pysssss, Text]
problems: []
missing: []
members: [图片生成/反推提示词/api直接反推_2063883890095382530.json, 图片生成/反推提示词/故事板出视频提示词_2069276070452482050.json, 图片生成/图生图/出故事板+故事板提示词_2069265955523485698.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_925

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/api直接反推_2063883890095382530.json、图片生成/反推提示词/故事板出视频提示词_2069276070452482050.json、图片生成/图生图/出故事板+故事板提示词_2069265955523485698.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `RHLLMChatNode`
- `SaveImage`
- `ShowText|pysssss`
- `Text`

**可变部分**（部分 workflow 才有）：
- `Save Text File` —— 2/3 个有
- `RHSettingsNode` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有
- `SaveText|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
