---
name: unknown_workflow_generic_1886
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.908
common_nodes: [Fast Groups Bypasser (rgthree), LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ColorPicker, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage]
problems: []
missing: []
members: [平台全量/BiRefNet BiRefNet 超细致背景抠图_1920327491515252738.json, 平台全量/BiRefNet 超细致抠图_1964829189230743553.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1886

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/BiRefNet BiRefNet 超细致背景抠图_1920327491515252738.json、平台全量/BiRefNet 超细致抠图_1964829189230743553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `BiRefNet_ModelLoader_Zho` —— 1/2 个有
- `BiRefNet_Zho` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
