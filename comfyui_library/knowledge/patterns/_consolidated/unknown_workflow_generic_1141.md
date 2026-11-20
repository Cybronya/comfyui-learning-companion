---
name: unknown_workflow_generic_1141
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.892667
common_nodes: [CXH_Leffa_Viton_Load, CXH_Leffa_Viton_Run, DensePosePreprocessor, LayerMask: MaskGrow, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Segformer+Leffa服装换装-简单高效_1944954799215529986.json, 平台全量/Leffa虚拟试穿和姿势转换 virtual try-on_1874011612846624769.json, 平台全量/最简单的服装迁移，只有几个节点_1935685991740923905.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1141

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Segformer+Leffa服装换装-简单高效_1944954799215529986.json、平台全量/Leffa虚拟试穿和姿势转换 virtual try-on_1874011612846624769.json、平台全量/最简单的服装迁移，只有几个节点_1935685991740923905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CXH_Leffa_Viton_Load`
- `CXH_Leffa_Viton_Run`
- `DensePosePreprocessor`
- `LayerMask: MaskGrow`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
