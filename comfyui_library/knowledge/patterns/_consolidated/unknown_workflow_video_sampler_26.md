---
name: unknown_workflow_video_sampler_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.91
common_nodes: [CM_FloatToInt, Image2Video, ImageFromBatch+, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, 加载视频路径, 视频缩放]
problems: []
missing: []
members: [视频生成/图生视频/DreamID-V视频换脸_2009168696912125953.json, 视频生成/图生视频/字节DreamID-V视频换脸_2009174630229090305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/DreamID-V视频换脸_2009168696912125953.json、视频生成/图生视频/字节DreamID-V视频换脸_2009174630229090305.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
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
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
