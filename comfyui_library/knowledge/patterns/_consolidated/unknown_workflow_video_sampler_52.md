---
name: unknown_workflow_video_sampler_52
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.900667
common_nodes: [CM_FloatToInt, Image2Video, ImageFromBatch+, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, 加载视频路径, 视频缩放]
problems: []
missing: []
members: [平台全量/字节DreamID-V视频换脸_2009131166686777346.json, 视频生成/图生视频/DreamID-V视频换脸_2009168696912125953.json, 视频生成/图生视频/字节DreamID-V视频换脸_2009174630229090305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/字节DreamID-V视频换脸_2009131166686777346.json、视频生成/图生视频/DreamID-V视频换脸_2009168696912125953.json、视频生成/图生视频/字节DreamID-V视频换脸_2009174630229090305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CM_FloatToInt`
- `Image2Video`
- `ImageFromBatch+`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `加载视频路径`
- `视频缩放`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
