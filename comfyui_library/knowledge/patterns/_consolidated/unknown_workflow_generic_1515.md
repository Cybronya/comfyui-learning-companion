---
name: unknown_workflow_generic_1515
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [Image Comparer (rgthree), ImageComposite+, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/宠物变假模特LORA数据集素材_1991486638113112066.json, 图片生成/图生图/宠物变假模特LORA数据集素材_1991497280823967746.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1515

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/宠物变假模特LORA数据集素材_1991486638113112066.json、图片生成/图生图/宠物变假模特LORA数据集素材_1991497280823967746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Rembg (Remove Background)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
