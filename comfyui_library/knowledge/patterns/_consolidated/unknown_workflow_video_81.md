---
name: unknown_workflow_video_81
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.473
common_nodes: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/视频转GIF图片_2011731899575705602.json, 平台全量/视频转GIF图片_2067129295868358658.json, 平台全量/视频转GIF图片_2071411440728231937.json, 视频生成/图生视频/实用工具-视频转GIF图片_2089752563230011394.json, 视频生成/图生视频/视频转gif-RH工作流主图专用_1975224669374689281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_81

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频转GIF图片_2011731899575705602.json、平台全量/视频转GIF图片_2067129295868358658.json、平台全量/视频转GIF图片_2071411440728231937.json、视频生成/图生视频/实用工具-视频转GIF图片_2089752563230011394.json、视频生成/图生视频/视频转gif-RH工作流主图专用_1975224669374689281.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 4/5 个有
- `LoadImage` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `UploadVideoToHost` —— 1/5 个有
- `VHS_LoadVideoFFmpegPath` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
