---
name: unknown_workflow_video_upscale_vae_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5405
common_nodes: [Fast Groups Bypasser (rgthree), FlashVSRNode, INTConstant, ImageScaleToTotalPixels, JWInteger, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: ["图片生成/图生图/三笔成书-最强视频修复合集 支持SeedVR2.5,FlashVSR_2008344998995038210.json", 数字人/数字人/视频高清放大  SeedVR2.5  + FlashVSR   视频补帧_2049019887674204161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/三笔成书-最强视频修复合集 支持SeedVR2.5,FlashVSR_2008344998995038210.json、数字人/数字人/视频高清放大  SeedVR2.5  + FlashVSR   视频补帧_2049019887674204161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `intToFloat _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
