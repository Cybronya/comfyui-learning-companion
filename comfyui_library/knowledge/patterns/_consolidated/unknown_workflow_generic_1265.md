---
name: unknown_workflow_generic_1265
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8255
common_nodes: [Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleToTotalPixels, LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap, easy compare, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2高清放大流_2003292714370260994.json, 图片生成/图生图/seedvr2 超高清无损放大 文字、人像等都非常给力_1975487646812213250.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1265

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2高清放大流_2003292714370260994.json、图片生成/图生图/seedvr2 超高清无损放大 文字、人像等都非常给力_1975487646812213250.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `easy compare`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
