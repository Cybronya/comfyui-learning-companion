---
name: unknown_workflow_video_inpaint
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.98225
common_nodes: [BboxDetectorCombined_v2, ImageBatchToList, LaMaInpaint, LoadLaMaModel, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageListToImageBatch]
problems: []
missing: []
members: [平台全量/全能视频S去水印+高清放大_2011722131675025410.json, 平台全量/全能视频S视频去水印（自动检测水印）_1985318835630784514.json, 平台全量/全能视频S视频去水印（自动检测水印）_1991867030498332674.json, 平台全量/大峰 全能视频S视频去水印（自动检测水印）_1985592566408261633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/全能视频S去水印+高清放大_2011722131675025410.json、平台全量/全能视频S视频去水印（自动检测水印）_1985318835630784514.json、平台全量/全能视频S视频去水印（自动检测水印）_1991867030498332674.json、平台全量/大峰 全能视频S视频去水印（自动检测水印）_1985592566408261633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `ImageBatchToList`
- `LaMaInpaint`
- `LoadLaMaModel`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
