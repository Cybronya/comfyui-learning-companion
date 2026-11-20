---
name: unknown_workflow_upscale_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.741
common_nodes: [ETN_ApplyMaskToImage, Float, Image Comparer (rgthree), ImageToMask, ImageUpscaleWithModel, InvertMask, JoinImageWithAlpha, LayerMask: MaskEdgeUltraDetail V2, LoadImage, PreviewImage, PrimitiveInt, SaveImageWithAlpha, SplitImageChannels, UpscaleModelLoader, preview_mask]
problems: []
missing: []
members: [平台全量/边缘细化工作流(参数开放修改)_2027652747738226690.json, 平台全量/边缘细化工作流(参数开放修改)_2028328341132021761.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/边缘细化工作流(参数开放修改)_2027652747738226690.json、平台全量/边缘细化工作流(参数开放修改)_2028328341132021761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `ETN_ApplyMaskToImage`
- `Float`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `InvertMask`
- `JoinImageWithAlpha`
- `LayerMask: MaskEdgeUltraDetail V2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImageWithAlpha`
- `SplitImageChannels`
- `UpscaleModelLoader`
- `preview_mask`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
