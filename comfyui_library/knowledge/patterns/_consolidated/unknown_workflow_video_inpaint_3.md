---
name: unknown_workflow_video_inpaint_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.841
common_nodes: [BboxDetectorCombined_v2, ImageConcanate, LaMaInpaint, LoadLaMaModel, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [平台全量/全能视频S去水印极速版（10秒只要1-2分钟，横竖都支持）_1984939423517261825.json, 平台全量/视频-全能视频S去水印_1985529170363039746.json, 视频生成/图生视频/【阡陌】全能视频S视频自动去水印_1988075729701285890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/全能视频S去水印极速版（10秒只要1-2分钟，横竖都支持）_1984939423517261825.json、平台全量/视频-全能视频S去水印_1985529170363039746.json、视频生成/图生视频/【阡陌】全能视频S视频自动去水印_1988075729701285890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `ImageConcanate`
- `LaMaInpaint`
- `LoadLaMaModel`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
