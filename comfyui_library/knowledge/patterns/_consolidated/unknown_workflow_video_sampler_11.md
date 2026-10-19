---
name: unknown_workflow_video_sampler_11
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.806
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/1977783912887898113.json, 视频生成/图生视频/1975893175250366465.json, 视频生成/图生视频/1974023372034191362.json, 视频生成/图生视频/1977048593158807553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1977783912887898113.json、视频生成/图生视频/1975893175250366465.json、视频生成/图生视频/1974023372034191362.json、视频生成/图生视频/1977048593158807553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `MaskToImage` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
