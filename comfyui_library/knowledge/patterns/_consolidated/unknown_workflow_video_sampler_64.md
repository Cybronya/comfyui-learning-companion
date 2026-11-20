---
name: unknown_workflow_video_sampler_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.789
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, Fast Groups Muter (rgthree), ImageConcanate, ImageFromBatch+, LoadImage, MaskToImage, Note Plus (mtb), Note _O, PreviewImage, RepeatImageBatch, SaveImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/(即梦16_9去水印)DiffuEraser视频字幕水印消除进阶工作流V3（支持音频）_1985758059693780993.json, 平台全量/DiffuEraser视频字幕水印消除进阶工作流V2（支持音频）_1904921330204987393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/(即梦16_9去水印)DiffuEraser视频字幕水印消除进阶工作流V3（支持音频）_1985758059693780993.json、平台全量/DiffuEraser视频字幕水印消除进阶工作流V2（支持音频）_1904921330204987393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Fast Groups Muter (rgthree)`
- `ImageConcanate`
- `ImageFromBatch+`
- `LoadImage`
- `MaskToImage`
- `Note Plus (mtb)`
- `Note _O`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any To Any` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
