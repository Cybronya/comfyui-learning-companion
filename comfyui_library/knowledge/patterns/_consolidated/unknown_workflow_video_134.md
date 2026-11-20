---
name: unknown_workflow_video_134
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.958333
common_nodes: [FlashVSRInitPipe, FlashVSRNodeAdv, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/FlashVSR 视频高清放大_2069736669586219010.json, 平台全量/FlashVSR(Ultra-Fast (Advanced))视频高清放大_2011625169525153793.json, 平台全量/flashvsr_mix_2027778761252413442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_134

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FlashVSR 视频高清放大_2069736669586219010.json、平台全量/FlashVSR(Ultra-Fast (Advanced))视频高清放大_2011625169525153793.json、平台全量/flashvsr_mix_2027778761252413442.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `FlashVSRInitPipe`
- `FlashVSRNodeAdv`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ImageFromBatch` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
