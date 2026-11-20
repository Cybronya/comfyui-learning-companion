---
name: unknown_workflow_generic_1401
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6135
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs]
problems: []
missing: []
members: [图片生成/图生图/Seedvr高清放大_1988909843182399489.json, 图片生成/图生图/seedVR2最强放大，细节还原夸张_1950769674688618497.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1401

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Seedvr高清放大_1988909843182399489.json、图片生成/图生图/seedVR2最强放大，细节还原夸张_1950769674688618497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
