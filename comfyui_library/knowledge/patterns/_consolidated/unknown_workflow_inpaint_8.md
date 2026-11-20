---
name: unknown_workflow_inpaint_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [InpaintCropImproved, LoadImage, PreviewImage, RH_Nano_Banana2_Image2Image, SaveImage]
problems: []
missing: []
members: [平台全量/一键模特换装_2077220946804559873.json, 平台全量/全能图片 Pro_2020749358190305281.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键模特换装_2077220946804559873.json、平台全量/全能图片 Pro_2020749358190305281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `InpaintCropImproved`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InpaintStitchImproved` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
