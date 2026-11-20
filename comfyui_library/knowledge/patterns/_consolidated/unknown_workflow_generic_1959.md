---
name: unknown_workflow_generic_1959
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9135
common_nodes: [CR Text, JoinImageWithAlpha, LayerMask: SegmentAnythingUltra V2, LoadImage, Mask Invert, MaskPreview+, RH_Translator, SDMatteApply, SaveImage]
problems: []
missing: []
members: [平台全量/快速抠图_2055219681165889537.json, 平台全量/毛茸茸+高清抠图，双图生成_2095796738048225281.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1959

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/快速抠图_2055219681165889537.json、平台全量/毛茸茸+高清抠图，双图生成_2095796738048225281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `JoinImageWithAlpha`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `Mask Invert`
- `MaskPreview+`
- `RH_Translator`
- `SDMatteApply`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `InspyrenetRembgAdvanced` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海图像组合批次` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
