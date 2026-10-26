---
name: unknown_workflow_generic_1582
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/高清放大_2078332474970689538.json, 图片生成/文生图/seedVR2 万物高清放大（分块）_2028449984504401922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1582

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清放大_2078332474970689538.json、图片生成/文生图/seedVR2 万物高清放大（分块）_2028449984504401922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 1/2 个有
- `Get Image Size` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `Int` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
