---
name: unknown_workflow_generic_1288
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.616
common_nodes: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, PreviewAny, SaveImage]
problems: []
missing: []
members: [图片生成/反推提示词/JoyCaption本地图片提示词反推_2101492268921352193.json, 图片生成/反推提示词/tonnie-joycaption反推和florence2的对比_1993649842232770561.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1288

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/JoyCaption本地图片提示词反推_2101492268921352193.json、图片生成/反推提示词/tonnie-joycaption反推和florence2的对比_1993649842232770561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `PreviewAny`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
