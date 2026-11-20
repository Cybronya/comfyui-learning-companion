---
name: unknown_workflow_video_sampler_25
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.945571
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, LoadImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏V2_1974043265089581057.json, 平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏V3_1974306441639104514.json, 平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏_1973722357393174530.json, 平台全量/视频去水印-DiffuEraser_1974743327083991042.json, 平台全量/高质量视频去水印_移除字幕_2113653593525014529.json, 平台全量/高质量视频去水印（附详细用法）_2110386106918330369.json, 视频生成/文生视频/全能视频S去水印_1977783912887898113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_25

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏V2_1974043265089581057.json、平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏V3_1974306441639104514.json、平台全量/视频去水印 全能视频S去水印 一键去水印 自动识别横竖屏_1973722357393174530.json、平台全量/视频去水印-DiffuEraser_1974743327083991042.json、平台全量/高质量视频去水印_移除字幕_2113653593525014529.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `LoadImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `Compare` —— 3/7 个有
- `MaskToImage` —— 3/7 个有
- `easy ifElse` —— 3/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
