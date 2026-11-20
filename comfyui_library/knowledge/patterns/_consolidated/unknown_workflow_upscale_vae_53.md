---
name: unknown_workflow_upscale_vae_53
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7915
common_nodes: [INTConstant, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/AA--Sparkvideo2.0创作辅助--视频获取首尾帧+4K放大修复_2020909658290003970.json, 平台全量/视频高清放大_2046516018679390210.json, 视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json, 视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_53

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/AA--Sparkvideo2.0创作辅助--视频获取首尾帧+4K放大修复_2020909658290003970.json、平台全量/视频高清放大_2046516018679390210.json、视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json、视频生成/文生视频/SeedVR2高清视频_2088119385247539202.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `INTConstant`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `SaveImage` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
