---
name: unknown_workflow_generic_1423
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.838
common_nodes: [LoadImage, ProcessString, RH_LLMAPI_Pro_Node, RH_RhartImageNG31FlashOfficialImageToImage, SaveImage, ShowText|pysssss, Text, easy promptConcat, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/电商主图详情图 超低价12图--全能图片2.0自动分割 经济版工作流_2103288022275026946.json, 图片生成/文生图/最新G image2电商主图工作流 V1.0_2092240232010829826.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1423

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商主图详情图 超低价12图--全能图片2.0自动分割 经济版工作流_2103288022275026946.json、图片生成/文生图/最新G image2电商主图工作流 V1.0_2092240232010829826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageNG31FlashOfficialImageToImage`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `easy promptConcat`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 1/2 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
