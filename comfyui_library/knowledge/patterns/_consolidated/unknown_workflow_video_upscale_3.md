---
name: unknown_workflow_video_upscale_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.837
common_nodes: [PDIMAGE_LongerSize, RTXVideoSuperResolution, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/视频超分 Vosr2 DLSS - 2K_2097129015567020033.json, 数字人/数字人/视频高清放大 Vosr 2 （1K-2K）_2097136348686807042.json, 视频生成/图生视频/minimax H3 Vosr 2.0超分修复专用2k流（无需plus）_2097566982299275265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/视频超分 Vosr2 DLSS - 2K_2097129015567020033.json、数字人/数字人/视频高清放大 Vosr 2 （1K-2K）_2097136348686807042.json、视频生成/图生视频/minimax H3 Vosr 2.0超分修复专用2k流（无需plus）_2097566982299275265.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `PDIMAGE_LongerSize`
- `RTXVideoSuperResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 2/3 个有
- `Int` —— 1/3 个有
- `RH_DLSS5Enhance` —— 1/3 个有
- `easy mathInt` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
