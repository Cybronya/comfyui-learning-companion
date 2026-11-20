---
name: unknown_workflow_generic_1987
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.697
common_nodes: [GetImageSize+, GuHai_IDPhotoCrop, ImageScaleToTotalPixels, RHHiddenNodes, SingleImageLayoutNode, easy imageSize, 孤海-自定义颜色, 孤海注释]
problems: []
missing: []
members: [平台全量/证件照片制作，自动裁切、抠图、换底、排版，识别人脸，倾斜自动校正_2058454263629697025.json, 平台全量/证件照片制作，自动裁切、抠图、换底、排版，识别人脸，倾斜自动校正_2058773893019693057.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1987

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/证件照片制作，自动裁切、抠图、换底、排版，识别人脸，倾斜自动校正_2058454263629697025.json、平台全量/证件照片制作，自动裁切、抠图、换底、排版，识别人脸，倾斜自动校正_2058773893019693057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `GuHai_IDPhotoCrop`
- `ImageScaleToTotalPixels`
- `RHHiddenNodes`
- `SingleImageLayoutNode`
- `easy imageSize`
- `孤海-自定义颜色`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHUploadZip_V2` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
