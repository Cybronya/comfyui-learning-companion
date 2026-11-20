---
name: unknown_workflow_generic_1962
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.67
common_nodes: [BRIAAI Matting, BiRefNet_ModelLoader_Zho, BiRefNet_Zho, InspyrenetRembgAdvanced, LayerMask: BiRefNetUltra, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LoadImage, PreviewImage, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [平台全量/抠图六君子（实用版）_1955499186869473282.json, 平台全量/抠图工作流在线合集COMFY UI_1932240006578864129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1962

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/抠图六君子（实用版）_1955499186869473282.json、平台全量/抠图工作流在线合集COMFY UI_1932240006578864129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `BRIAAI Matting`
- `BiRefNet_ModelLoader_Zho`
- `BiRefNet_Zho`
- `InspyrenetRembgAdvanced`
- `LayerMask: BiRefNetUltra`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
