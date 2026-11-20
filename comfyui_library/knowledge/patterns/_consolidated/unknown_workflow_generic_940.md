---
name: unknown_workflow_generic_940
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.486667
common_nodes: [DebugTensorShape+, Float, ImageScaleBy, InvertMask, JWImageResizeByShorterSide, JoinImageWithAlpha, LayerMask: BiRefNetUltra, LayerMask: MaskPreview, LoadImage, PreviewImage, ResizeMask, SaveImage, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/4K以上超清大图多阶段抠图工作流V1_1952200847826563074.json, 图片生成/图生图/BenUltra 4K抠图v1_2066126877932220418.json, 图片生成/图生图/（能力层调用）抠图v1_2065999798217564162.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_940

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/4K以上超清大图多阶段抠图工作流V1_1952200847826563074.json、图片生成/图生图/BenUltra 4K抠图v1_2066126877932220418.json、图片生成/图生图/（能力层调用）抠图v1_2065999798217564162.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `DebugTensorShape+`
- `Float`
- `ImageScaleBy`
- `InvertMask`
- `JWImageResizeByShorterSide`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltra`
- `LayerMask: MaskPreview`
- `LoadImage`
- `PreviewImage`
- `ResizeMask`
- `SaveImage`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerMask: BenUltra` —— 2/3 个有
- `LayerMask: LoadBenModel` —— 2/3 个有
- `LayerMask: RmBgUltra V2` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
