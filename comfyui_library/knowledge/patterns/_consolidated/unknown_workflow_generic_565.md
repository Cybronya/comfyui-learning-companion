---
name: unknown_workflow_generic_565
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.792667
common_nodes: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键抠图_2003409017785491457.json, 图片生成/图生图/一键移除背景+全节点注释_2056956775504637954.json, 图片生成/图生图/最强一键抠图_抠图去除背景_2088971186419093506.json, 平台全量/台挂历抠图工作流_2063802342654431234.json, 平台全量/抠图_2043536305446981633.json, 平台全量/最强抠图·快捷抠图_2049373427810705410.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_565

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键抠图_2003409017785491457.json、图片生成/图生图/一键移除背景+全节点注释_2056956775504637954.json、图片生成/图生图/最强一键抠图_抠图去除背景_2088971186419093506.json、平台全量/台挂历抠图工作流_2063802342654431234.json、平台全量/抠图_2043536305446981633.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorPicker` —— 5/6 个有
- `InspyrenetRembg` —— 4/6 个有
- `LayerUtility: ImageCombineAlpha` —— 3/6 个有
- `MaskPreview+` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
