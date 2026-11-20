---
name: unknown_workflow_video_sampler_11
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.826364
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/万能去水印+自动水印定位版+全节点注释_2058078052843868161.json, 平台全量/去全能视频S最新水印（水印位置：左边2个，右边1个）_1985272896941662210.json, 平台全量/固定位置去除水印（需要上传首帧绘制蒙版）_2034666743020392450.json, 平台全量/成功率超高！全能视频S去水印（支持横屏竖屏）_1976887446711554049.json, 平台全量/成功率超高！去全能视频S最新水印（支持横屏竖屏）_1984084622239793153.json, 平台全量/成功率超高！去全能视频S最新水印（支持横屏竖屏）_1985256120207949825.json, 平台全量/成功率超高！去全能视频S最新水印（支持横屏竖屏）_1985280569347088385.json, 平台全量/最新全能视频S去水印（支持横屏竖屏）_1975093275969368065.json, 视频生成/图生视频/全能视频S横屏视频动态去水印消除（保留音频）_1975893175250366465.json, 视频生成/图生视频/全能视频S视频工具2：一键去水印（速度快、注意选择横屏还是竖屏）_1974023372034191362.json, 视频生成/图生视频/视频去水印_1977048593158807553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/万能去水印+自动水印定位版+全节点注释_2058078052843868161.json、平台全量/去全能视频S最新水印（水印位置：左边2个，右边1个）_1985272896941662210.json、平台全量/固定位置去除水印（需要上传首帧绘制蒙版）_2034666743020392450.json、平台全量/成功率超高！全能视频S去水印（支持横屏竖屏）_1976887446711554049.json、平台全量/成功率超高！去全能视频S最新水印（支持横屏竖屏）_1984084622239793153.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 10/11 个有
- `RepeatImageBatch` —— 10/11 个有
- `JWInteger` —— 9/11 个有
- `easy ifElse` —— 7/11 个有
- `RHHiddenNodes` —— 6/11 个有
- `easy compare` —— 6/11 个有
- `easy showAnything` —— 4/11 个有
- `ImageConcanate` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `SAM3Segment` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
