---
name: unknown_workflow_generic_1708
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.629
common_nodes: [AnyLineArtPreprocessor_aux, ImageBlend, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LoadImage, PreviewImage, SaveImage, Simple String, easy imagePixelPerfect]
problems: []
missing: []
members: [图片生成/图生图/图像光绘描边 创意风格_1944727334161403906.json, 平台全量/线条滑板少女_1810569625838006274.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1708

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图像光绘描边 创意风格_1944727334161403906.json、平台全量/线条滑板少女_1810569625838006274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `ImageBlend`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Simple String`
- `easy imagePixelPerfect`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerUtility: ImageOpacity` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
