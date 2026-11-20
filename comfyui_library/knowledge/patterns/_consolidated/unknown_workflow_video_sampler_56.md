---
name: unknown_workflow_video_sampler_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.911667
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, Int, LayerUtility: ImageScaleByAspectRatio V2, MaskToImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频去水印V1（快速版）_2022943955473670146.json, 平台全量/视频去水印_2029386903010676737.json, 平台全量/视频去物擦除移除-全自动_2022201557751701506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频去水印V1（快速版）_2022943955473670146.json、平台全量/视频去水印_2029386903010676737.json、平台全量/视频去物擦除移除-全自动_2022201557751701506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskToImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `easy int` —— 2/3 个有
- `BiRefNet_Hugo` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `RepeatImageBatch` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
