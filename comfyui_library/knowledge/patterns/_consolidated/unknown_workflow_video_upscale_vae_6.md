---
name: unknown_workflow_video_upscale_vae_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6665
common_nodes: [INTConstant, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json, 视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json、视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `INTConstant`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
