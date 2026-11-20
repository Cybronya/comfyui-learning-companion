---
name: unknown_workflow_sampler_113
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7285
common_nodes: [ImageCompositeMasked, ImageRemoveBackground+, ImageResizeKJv2, LBMSampler, LoadImage, LoadLBMModel, PreviewImage, SaveImage, TransparentBGSession+]
problems: []
missing: []
members: [平台全量/超强融图自动打光LBM_relight 最新工作流_1922923185380147201.json, 视频生成/图生视频/LBM-换背景的重打光优化_1922624982000746497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/超强融图自动打光LBM_relight 最新工作流_1922923185380147201.json、视频生成/图生视频/LBM-换背景的重打光优化_1922624982000746497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageCompositeMasked`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `LBMSampler`
- `LoadImage`
- `LoadLBMModel`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
