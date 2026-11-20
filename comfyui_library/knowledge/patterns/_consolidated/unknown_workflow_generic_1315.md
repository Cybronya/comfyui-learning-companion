---
name: unknown_workflow_generic_1315
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.77
common_nodes: [DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Florence2Run, Florence2toCoordinates, GrowMask, Image Rembg (Remove Background), Image Remove Background Rembg (mtb), ImageAndMaskPreview, ImageResize+, InspyrenetRembg, InvertMask, LayerMask: SegmentAnythingUltra V2, LoadImage, MaskPreview+, MaskToImage, PreviewImage, Sam2Segmentation, SaveImage, easy imageRemBg, ttN imageREMBG]
problems: []
missing: []
members: [平台全量/抠图背景移除节点对比_1825807159816032257.json, 平台全量/背景移除节点对比_1820333233749037057.json, 平台全量/背景移除节点对比_1820797600005296129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1315

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/抠图背景移除节点对比_1825807159816032257.json、平台全量/背景移除节点对比_1820333233749037057.json、平台全量/背景移除节点对比_1820797600005296129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMask`
- `Image Rembg (Remove Background)`
- `Image Remove Background Rembg (mtb)`
- `ImageAndMaskPreview`
- `ImageResize+`
- `InspyrenetRembg`
- `InvertMask`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `Sam2Segmentation`
- `SaveImage`
- `easy imageRemBg`
- `ttN imageREMBG`

**可变部分**（部分 workflow 才有）：
- `easy getNode` —— 2/3 个有
- `easy setNode` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
