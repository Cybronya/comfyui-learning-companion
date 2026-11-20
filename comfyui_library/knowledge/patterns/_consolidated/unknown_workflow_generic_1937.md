---
name: unknown_workflow_generic_1937
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.694
common_nodes: [Bounded Image Crop with Mask, ImageStitch, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Translator, SaveImage, SaveImagePlus]
problems: []
missing: []
members: [平台全量/全能图片V1-HZ_1981200926629421058.json, 平台全量/全能图片V12.0-HZ_1998568098355666946.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1937

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全能图片V1-HZ_1981200926629421058.json、平台全量/全能图片V12.0-HZ_1998568098355666946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Bounded Image Crop with Mask`
- `ImageStitch`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `SaveImagePlus`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
