---
name: unknown_workflow_generic_1282
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [GH_MaskCropV2, GoohaiUniversalSlider, GrowMaskWithBlur, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskPreview, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/lora制作 _ 裁剪+主体白模_2102266406212554754.json, 图片生成/图生图/lora制作_裁剪+主体白模_2102305971107352577.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1282

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/lora制作 _ 裁剪+主体白模_2102266406212554754.json、图片生成/图生图/lora制作_裁剪+主体白模_2102305971107352577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `GH_MaskCropV2`
- `GoohaiUniversalSlider`
- `GrowMaskWithBlur`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
