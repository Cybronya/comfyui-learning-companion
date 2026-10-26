---
name: unknown_workflow_sampler_49
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RunningHub ICCustom Loader, RunningHub ICCustom Sampler, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/35.tonnie-IC Custom万物迁移（效果不好）_2003457255477526529.json, 图片生成/图生图/IC-Custom万物迁移_1970427324682432514.json, 图片生成/图生图/IC-Custom万物迁移单图参考V1_1970424642190123009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/35.tonnie-IC Custom万物迁移（效果不好）_2003457255477526529.json、图片生成/图生图/IC-Custom万物迁移_1970427324682432514.json、图片生成/图生图/IC-Custom万物迁移单图参考V1_1970424642190123009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RunningHub ICCustom Loader`
- `RunningHub ICCustom Sampler`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: CropByMask V2` —— 2/3 个有
- `LoadImageFromUrl` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `MaskFillHoles` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
