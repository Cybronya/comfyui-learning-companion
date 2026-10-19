---
name: unknown_workflow_video_70
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6005
common_nodes: [CR String To Combo, CR Text Concatenate, ImpactStringSelector, ImpactSwitch, Int, LayerUtility: ImageMaskScaleAs, LoadImage, MathExpression|pysssss, PrimitiveBoolean, PrimitiveString, TransitionImagesMulti, VHS_VideoCombine]
problems: []
missing: [CR String To Combo, CR Text Concatenate, LayerUtility: ImageMaskScaleAs, MathExpression|pysssss]
members: [图片生成/文生图/1943525069970677762.json, 视频生成/图生视频/1943498791872065538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1943525069970677762.json、视频生成/图生视频/1943498791872065538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `CR String To Combo`
- `CR Text Concatenate`
- `ImpactStringSelector`
- `ImpactSwitch`
- `Int`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `PrimitiveString`
- `TransitionImagesMulti`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR String To Combo、CR Text Concatenate、LayerUtility: ImageMaskScaleAs、MathExpression|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
