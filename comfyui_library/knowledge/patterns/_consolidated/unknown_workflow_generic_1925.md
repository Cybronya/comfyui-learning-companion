---
name: unknown_workflow_generic_1925
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8895
common_nodes: [BOOLConstant, GetImagesFromBatchIndexed, INTConstant, ImageListToImageBatch, ImageToMask, ImpactMakeImageList, InspyrenetRembg, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LoadImage, Mask Fill Holes, MaskFix+, RMBG, SaveImage, SplitImageWithAlpha, easy cleanGpuUsed, easy ifElse, easy imageCropFromMask, easy imageSwitch, easy isMaskEmpty]
problems: []
missing: []
members: [平台全量/【星汇工作流】抠图大师_1909925312988413953.json, 平台全量/最强指定位置扣图（三种算法三张图）_1920448418496315393.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1925

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【星汇工作流】抠图大师_1909925312988413953.json、平台全量/最强指定位置扣图（三种算法三张图）_1920448418496315393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BOOLConstant`
- `GetImagesFromBatchIndexed`
- `INTConstant`
- `ImageListToImageBatch`
- `ImageToMask`
- `ImpactMakeImageList`
- `InspyrenetRembg`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `Mask Fill Holes`
- `MaskFix+`
- `RMBG`
- `SaveImage`
- `SplitImageWithAlpha`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageCropFromMask`
- `easy imageSwitch`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageBatchToList+` —— 1/2 个有
- `LayerUtility: GetImageSize` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
