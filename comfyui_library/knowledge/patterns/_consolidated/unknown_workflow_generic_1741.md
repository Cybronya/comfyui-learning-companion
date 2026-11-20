---
name: unknown_workflow_generic_1741
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.764
common_nodes: [Bjornulf_ShowInt, Image Comparer (rgthree), ImageScaleToTotalPixels, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, SeedVR2, SeedVR2BlockSwap, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/批量高清微放大_1978388995535212546.json, 平台全量/批量放大-seedvr2_1988137660365565954.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1741

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量高清微放大_1978388995535212546.json、平台全量/批量放大-seedvr2_1988137660365565954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Get Image Size` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleDownToSize` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
