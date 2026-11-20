---
name: unknown_workflow_unet
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.848
common_nodes: [CR Simple Image Compare, LayerUtility: ImageBlendAdvance, LoadImage, PreviewImage, RHHiddenNodes, SaveImage]
problems: []
missing: []
members: [平台全量/Ultimate 鞋模大师_发布版_1888204332104310785.json, 平台全量/虚拟试鞋 Virtual Shoes Try-ON_1874995042531061761.json, 平台全量/鞋模大师_发布版_1876825803685351425.json]
source: knowledge_consolidation
---

# unknown_workflow_unet

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Ultimate 鞋模大师_发布版_1888204332104310785.json、平台全量/虚拟试鞋 Virtual Shoes Try-ON_1874995042531061761.json、平台全量/鞋模大师_发布版_1876825803685351425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Simple Image Compare`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DF_Image_scale_to_side` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Image Blank` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `FluxEmptyLatentSizePicker` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.96MP) - 3:4 | - | 1 | 100% |
| 高度 | 3 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
