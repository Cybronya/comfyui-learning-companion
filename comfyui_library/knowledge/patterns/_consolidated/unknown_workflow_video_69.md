---
name: unknown_workflow_video_69
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7164
common_nodes: [AILab_MaskPreview, CR Prompt Text, DF_Get_image_size, GetImageRangeFromBatch, JWInteger, MaskToImage, PDIMAGE_LongerSize, PreviewImage, SegmentV2, SolidColorBatched, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/(修复版)MatAnyone2视频抠像极速版V2_2036110565164191745.json, 平台全量/MatAnyone2视频抠像_2062730484035182594.json, 平台全量/MatAnyone2视频抠像极速版V1工作流_2036298141548421122.json, 平台全量/MatAnyone2视频抠蒙版_2036803418379001858.json, 数字人/数字人/MatAnyone2视频抠像_2037438476425105409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_69

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/(修复版)MatAnyone2视频抠像极速版V2_2036110565164191745.json、平台全量/MatAnyone2视频抠像_2062730484035182594.json、平台全量/MatAnyone2视频抠像极速版V1工作流_2036298141548421122.json、平台全量/MatAnyone2视频抠蒙版_2036803418379001858.json、数字人/数字人/MatAnyone2视频抠像_2037438476425105409.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_MaskPreview`
- `CR Prompt Text`
- `DF_Get_image_size`
- `GetImageRangeFromBatch`
- `JWInteger`
- `MaskToImage`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `SegmentV2`
- `SolidColorBatched`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `MatAnyone2` —— 3/5 个有
- `MatAnyoneVideoMatting` —— 2/5 个有
- `AudioToPath` —— 1/5 个有
- `JoinImageWithAlpha` —— 1/5 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/5 个有
- `RemoveAlphaChannel` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `SaveMatAnyone2TransparentMOV` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
