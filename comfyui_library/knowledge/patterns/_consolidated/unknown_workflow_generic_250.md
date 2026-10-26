---
name: unknown_workflow_generic_250
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.724667
common_nodes: [LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap]
problems: []
missing: []
members: [图片生成/图生图/seedVR2 原模无分快版本（放大参数低于4k时使用，速度最快）+全节点注释_2054878701971623938.json, 图片生成/图生图/“SeedVR2 图片高清放大”_1967493832130564098.json, 图片生成/图生图/图像无损高清放大_1956239087894188033.json, 图片生成/图生图/图像无损高清放大_2059279536960917505.json, 图片生成/图生图/图像超分-10-23-SeedVR-image-upscaler_1981316602547396610.json, 图片生成/图生图/最佳放大工作流：SeedVR2_bole_1956324968839741442.json, 图片生成/图生图/最强一致性高清放大：SeedVR2_1975560945038700545.json, 图片生成/图生图/最强一致性高清放大：SeedVR2_1997925676596494338.json, 图片生成/文生图/SeedVR2 高清无损放大_1965606007600762881.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_250

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/seedVR2 原模无分快版本（放大参数低于4k时使用，速度最快）+全节点注释_2054878701971623938.json、图片生成/图生图/“SeedVR2 图片高清放大”_1967493832130564098.json、图片生成/图生图/图像无损高清放大_1956239087894188033.json、图片生成/图生图/图像无损高清放大_2059279536960917505.json、图片生成/图生图/图像超分-10-23-SeedVR-image-upscaler_1981316602547396610.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `Int` —— 2/9 个有
- `PrimitiveInt` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
