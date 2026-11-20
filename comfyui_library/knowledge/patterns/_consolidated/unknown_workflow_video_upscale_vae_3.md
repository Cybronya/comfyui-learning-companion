---
name: unknown_workflow_video_upscale_vae_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847333
common_nodes: [CM_FloatToInt, CM_IntToFloat, Fast Groups Bypasser (rgthree), FlashVSRNode, ImageScaleToTotalPixels, RTXVideoSuperResolution, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/【极速视频放大】FlashVR 工业级短视频生产流水线视频放大_2032402915746390017.json, 视频生成/图生视频/【视频放大——遗珍重塑】SeedVR 语义级超清视频放大修复大片_2033193391764283393.json, 视频生成/图生视频/【视频放大硬件之光】NVIDIA RTX VSR 底层硬件级视界增强视频放大_2033193385128894465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【极速视频放大】FlashVR 工业级短视频生产流水线视频放大_2032402915746390017.json、视频生成/图生视频/【视频放大——遗珍重塑】SeedVR 语义级超清视频放大修复大片_2033193391764283393.json、视频生成/图生视频/【视频放大硬件之光】NVIDIA RTX VSR 底层硬件级视界增强视频放大_2033193385128894465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CM_FloatToInt`
- `CM_IntToFloat`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `ImageScaleToTotalPixels`
- `RTXVideoSuperResolution`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `ShowAnything|Mie` —— 2/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
