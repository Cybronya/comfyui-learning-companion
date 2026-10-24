---
name: unknown_workflow_video_upscale_vae_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [FlashVSRNode, GetImageRangeFromBatch, Image Comparer (rgthree), Int, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105122701890375682.json, 图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105499952859402242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105122701890375682.json、图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105499952859402242.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `FlashVSRNode`
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `Int`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
