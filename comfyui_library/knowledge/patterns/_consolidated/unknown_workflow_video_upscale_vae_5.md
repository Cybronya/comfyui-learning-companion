---
name: unknown_workflow_video_upscale_vae_5
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85725
common_nodes: [FlashVSRNode, Image Comparer (rgthree), JWInteger, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105122701890375682.json, 图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105499952859402242.json, 平台全量/@SeedVR2-视频超分_2053318242181103617.json, 平台全量/Flash VSR & SeedVR2.5-视频超分辨率-视频放大_2089362719114874881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105122701890375682.json、图片生成/图生图/Flash_VSR_&_SeedVR2.5-视频超分辨率-视频放大_2105499952859402242.json、平台全量/@SeedVR2-视频超分_2053318242181103617.json、平台全量/Flash VSR & SeedVR2.5-视频超分辨率-视频放大_2089362719114874881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `FlashVSRNode`
- `Image Comparer (rgthree)`
- `JWInteger`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 3/4 个有
- `Int` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `INTConstant` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
