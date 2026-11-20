---
name: unknown_workflow_generic_601
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.732833
common_nodes: [BiRefNet_Hugo, CR Color Panel, FaceAnalysisModels, FaceBoundingBox, GetNode, ImageCompositeMasked, ImageConcanate, ImageGenResolutionFromImage, ImageResizeKJv2, ImageToMask, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SetNode]
problems: []
missing: []
members: [平台全量/FashionX 单人摄影 0401_2039152943357759489.json, 平台全量/FashionX 单人摄影 纯色背景_2039211379160260610.json, 平台全量/三人组合动作 0403_2039912087048163330.json, 平台全量/单人摄影-1宫格-纯色背景_2039949002715697154.json, 平台全量/双人组合动作0402_2039635721920716802.json, 平台全量/自动驱动多人0403_2039990107574378498.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_601

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/FashionX 单人摄影 0401_2039152943357759489.json、平台全量/FashionX 单人摄影 纯色背景_2039211379160260610.json、平台全量/三人组合动作 0403_2039912087048163330.json、平台全量/单人摄影-1宫格-纯色背景_2039949002715697154.json、平台全量/双人组合动作0402_2039635721920716802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `BiRefNet_Hugo`
- `CR Color Panel`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GetNode`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageGenResolutionFromImage`
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SetNode`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/6 个有
- `LayerUtility: ColorImage V2` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Text Concatenate` —— 5/6 个有
- `ImageFromBatch+` —— 4/6 个有
- `RH_Nano_Banana2_Image2Image` —— 4/6 个有
- `ImageBatchMulti` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `easy imageSplitGrid` —— 2/6 个有
- `Int` —— 1/6 个有
- `String` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
