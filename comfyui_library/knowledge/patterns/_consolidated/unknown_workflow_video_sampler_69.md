---
name: unknown_workflow_video_sampler_69
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJ, LoadImage, MaskToImage, MathExpression|pysssss, PreviewImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/DiffuEraser视频去水印_1912104278100537346.json, 平台全量/视频去固定水印-DiffuEraser_1909519687481499649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_69

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/DiffuEraser视频去水印_1912104278100537346.json、平台全量/视频去固定水印-DiffuEraser_1909519687481499649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJ`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Note _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
