---
name: unknown_workflow_video_sampler_38
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CogVideoDecode, CogVideoImageEncode, CogVideoSampler, CogVideoTextEncode, DownloadAndLoadCogVideoModel, GetImageSizeAndCount, ImageResizeKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/CogVideoX-5B 从视频生成视频_1831296132877307905.json, 平台全量/CogVideoX-5B（视频到视频、视频动作、运动轨迹迁移）_1991346321957433345.json, 平台全量/CogVideoX-5B（视频到视频）_1905077086107930625.json, 视频生成/图生视频/CogVideoX_Fun_Pose 通过Pose控制视频生成_1844685380640493570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/CogVideoX-5B 从视频生成视频_1831296132877307905.json、平台全量/CogVideoX-5B（视频到视频、视频动作、运动轨迹迁移）_1991346321957433345.json、平台全量/CogVideoX-5B（视频到视频）_1905077086107930625.json、视频生成/图生视频/CogVideoX_Fun_Pose 通过Pose控制视频生成_1844685380640493570.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CogVideoDecode`
- `CogVideoImageEncode`
- `CogVideoSampler`
- `CogVideoTextEncode`
- `DownloadAndLoadCogVideoModel`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `WidgetToString` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
