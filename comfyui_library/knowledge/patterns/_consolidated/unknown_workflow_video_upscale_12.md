---
name: unknown_workflow_video_upscale_12
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.925
common_nodes: [PDIMAGE_LongerSize, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [平台全量/VOSR 2-视频高清放大_2097181313454403586.json, 平台全量/VOSR 2.0 Upscale 视频高清修复_2099368354850099201.json, 平台全量/VOSR2+DLSS5-视频高清放大_2097294637756141570.json, 平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json, 视频生成/图生视频/minimax H3 Vosr 2.0超分修复专用2k流（无需plus）_2097566982299275265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/VOSR 2-视频高清放大_2097181313454403586.json、平台全量/VOSR 2.0 Upscale 视频高清修复_2099368354850099201.json、平台全量/VOSR2+DLSS5-视频高清放大_2097294637756141570.json、平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json、视频生成/图生视频/minimax H3 Vosr 2.0超分修复专用2k流（无需plus）_2097566982299275265.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `PDIMAGE_LongerSize`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/5 个有
- `RTXVideoSuperResolution` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `GetNode` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `RH_DLSS5Enhance` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy mathInt` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
