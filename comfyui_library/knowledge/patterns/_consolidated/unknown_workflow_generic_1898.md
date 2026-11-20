---
name: unknown_workflow_generic_1898
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [LayerMask: MaskPreview, LayerUtility: ImageBlendAdvance, LoadImage, SaveImage]
problems: []
missing: []
members: [平台全量/Image Blend Advance节点示例 image_blend_advance_exampl_1899407927067758593.json, 平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1898

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Image Blend Advance节点示例 image_blend_advance_exampl_1899407927067758593.json、平台全量/遮罩区域检测 工作流示例 mask_box_detect_example_1899801314287562754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerMask: MaskPreview`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskBoxDetect` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
