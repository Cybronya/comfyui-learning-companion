---
name: unknown_workflow_inpaint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.757
common_nodes: [ColorMatchV2, GetImageSize, ImageResizeKJv2, InpaintCropImproved, InpaintStitchImproved, LoadImage, PreviewImage, PrimitiveStringMultiline, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能图片2+局部编辑_2078520596018843649.json, 图片生成/图生图/换装-局部编辑（全能图片pro）_2104810928310145025.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片2+局部编辑_2078520596018843649.json、图片生成/图生图/换装-局部编辑（全能图片pro）_2104810928310145025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatchV2`
- `GetImageSize`
- `ImageResizeKJv2`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/2 个有
- `RH_RhartImageNProEdit` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
