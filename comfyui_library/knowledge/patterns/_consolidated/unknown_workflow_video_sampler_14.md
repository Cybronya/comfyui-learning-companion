---
name: unknown_workflow_video_sampler_14
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.72275
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/即梦去水印-（9_16竖版）_2040101639603884034.json, 视频生成/图生视频/全能视频S横屏视频动态去水印消除（保留音频）_1975893175250366465.json, 视频生成/图生视频/全能视频S视频工具2：一键去水印（速度快、注意选择横屏还是竖屏）_1974023372034191362.json, 视频生成/图生视频/视频去水印_1977048593158807553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/即梦去水印-（9_16竖版）_2040101639603884034.json、视频生成/图生视频/全能视频S横屏视频动态去水印消除（保留音频）_1975893175250366465.json、视频生成/图生视频/全能视频S视频工具2：一键去水印（速度快、注意选择横屏还是竖屏）_1974023372034191362.json、视频生成/图生视频/视频去水印_1977048593158807553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `CustomAddLabel` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
