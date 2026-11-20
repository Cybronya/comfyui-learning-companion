---
name: unknown_workflow_generic_1608
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.825
common_nodes: [ImageCombineAlpha_UTK, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, SDMatteApply, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SDMatte最强抠图工作流 抠得很精细 嘎嘎好用_1971100907129737217.json, 平台全量/SDMatte最强抠图_1956920136835981314.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1608

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SDMatte最强抠图工作流 抠得很精细 嘎嘎好用_1971100907129737217.json、平台全量/SDMatte最强抠图_1956920136835981314.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageCombineAlpha_UTK`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `SDMatteApply`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
