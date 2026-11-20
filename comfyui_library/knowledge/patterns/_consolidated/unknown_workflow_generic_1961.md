---
name: unknown_workflow_generic_1961
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7755
common_nodes: [Bjornulf_ShowInt, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, RH_Nano_Banana2_Image2Image, SaveImage, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [平台全量/批量跑全能图片pro_2016717652802150402.json, 平台全量/空白工作流_2056940934306287618.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1961

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/批量跑全能图片pro_2016717652802150402.json、平台全量/空白工作流_2056940934306287618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
