---
name: unknown_workflow_upscale_42
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [ImageScaleToTotalPixels, ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/千府AI四次精细锐化一键工作流_1964911021498449921.json, 图片生成/图生图/无损图片高清放大_1951277904246288385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千府AI四次精细锐化一键工作流_1964911021498449921.json、图片生成/图生图/无损图片高清放大_1951277904246288385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
