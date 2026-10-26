---
name: unknown_workflow_vae_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.871
common_nodes: [ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SaveImagePlusV2, LoadImage, Mask Fill Holes, PrimitiveInt, RHHiddenNodes, SaveImage, VAEDecode]
problems: []
missing: []
members: [数字人/数字人/人物参考替换+动作参考_1970513906546450433.json, 数字人/数字人/多人动作迁移使用版_1970682012883427329.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/人物参考替换+动作参考_1970513906546450433.json、数字人/数字人/多人动作迁移使用版_1970682012883427329.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: SaveImagePlusV2`
- `LoadImage`
- `Mask Fill Holes`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SaveImage`
- `VAEDecode`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
