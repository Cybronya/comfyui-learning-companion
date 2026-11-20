---
name: unknown_workflow_generic_983
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.872333
common_nodes: [Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, easy int]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2放大_1990990820545372161.json, 图片生成/图生图/图片放大Image Upscaling_2038075311220330497.json, 图片生成/图生图/图片放大Image Upscaling_2052211583018913793.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_983

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeedVR2放大_1990990820545372161.json、图片生成/图生图/图片放大Image Upscaling_2038075311220330497.json、图片生成/图生图/图片放大Image Upscaling_2052211583018913793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `easy compare` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
