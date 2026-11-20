---
name: unknown_workflow_generic_1981
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [Astra, ImageFromBatch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, SaveVideo, 获取视频信息]
problems: []
missing: []
members: [平台全量/视频Topaz Video 高清放大_2100799326112014338.json, 平台全量/视频超分 4K Topaz Video 高清放大+全节点注释_2101673852165251074.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1981

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频Topaz Video 高清放大_2100799326112014338.json、平台全量/视频超分 4K Topaz Video 高清放大+全节点注释_2101673852165251074.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Astra`
- `ImageFromBatch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadVideo`
- `SaveVideo`
- `获取视频信息`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
