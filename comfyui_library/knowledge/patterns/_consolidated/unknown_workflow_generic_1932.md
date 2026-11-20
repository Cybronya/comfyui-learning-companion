---
name: unknown_workflow_generic_1932
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.647
common_nodes: [DetailTransfer, Image Comparer (rgthree), ImageToMask, ImpactGaussianBlurMask, LayerColor: Brightness & Contrast, LayerColor: Levels, LayerFilter: SkinBeauty, LayerUtility: ImageBlend, LayerUtility: ImageChannelSplit, LoadImage, MaskPreview+, PreviewImage, SaveImage]
problems: []
missing: []
members: [平台全量/人像去油美白_1890303332500774913.json, 平台全量/人像摄影_美白祛油_1934474700515078145.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1932

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人像去油美白_1890303332500774913.json、平台全量/人像摄影_美白祛油_1934474700515078145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `DetailTransfer`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `LayerColor: Brightness & Contrast`
- `LayerColor: Levels`
- `LayerFilter: SkinBeauty`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageChannelSplit`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
