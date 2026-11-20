---
name: unknown_workflow_video_upscale_15
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.812
common_nodes: [CM_IntToFloat, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageScale, ImageUpscaleWithModel, PrimitiveInt, SimpleMath+, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频补帧+高清放大视频专用_1953020586345828354.json, 平台全量/视频高清放大+补帧_2072521437788852225.json, 平台全量/视频高清放大+补帧_2072522981561159682.json, 平台全量/视频高清放大+补帧_2072524286971179009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频补帧+高清放大视频专用_1953020586345828354.json、平台全量/视频高清放大+补帧_2072521437788852225.json、平台全量/视频高清放大+补帧_2072522981561159682.json、平台全量/视频高清放大+补帧_2072524286971179009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CM_IntToFloat`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageScale`
- `ImageUpscaleWithModel`
- `PrimitiveInt`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
