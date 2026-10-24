---
name: unknown_workflow_video_upscale_vae_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.604667
common_nodes: [INTConstant, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: ["图片生成/图生图/三笔成书-最强视频修复合集 支持SeedVR2.5,FlashVSR_2008344998995038210.json", 视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json, 视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/三笔成书-最强视频修复合集 支持SeedVR2.5,FlashVSR_2008344998995038210.json、视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json、视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `INTConstant`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FlashVSRNode` —— 1/3 个有
- `JWInteger` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
