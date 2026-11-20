---
name: unknown_workflow_generic_1742
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [AutoDownloadBiRefNetModel, LayerUtility: ImageRemoveAlpha, LoadImage, PreviewImage, RembgByBiRefNet, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/抠图保存PNG或者指定底JPG_2054474779054362626.json, 平台全量/抠图保存PNG或JPG格式_2077589265768341505.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1742

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/抠图保存PNG或者指定底JPG_2054474779054362626.json、平台全量/抠图保存PNG或JPG格式_2077589265768341505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `AutoDownloadBiRefNetModel`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `PreviewImage`
- `RembgByBiRefNet`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
