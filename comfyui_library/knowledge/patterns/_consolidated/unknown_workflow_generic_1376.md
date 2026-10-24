---
name: unknown_workflow_generic_1376
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8355
common_nodes: [EmptyImage, Fast Groups Muter (rgthree), GeminiImageNode, GetImageSize, ImageCompositeMasked, ImageConcatMulti, ImagePadForOutpaintMasked_UTK, ImagePadKJ, ImageResizeKJ, ImageTextOverlay, Int, LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, SaveImage, TTP_text_mix]
problems: []
missing: []
members: [图片生成/图生图/大香蕉-全能图片V1 应用合集_1963466085067739137.json, 视频生成/图生视频/-全能图片V1 玩法合集_1971482222584905730.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1376

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/大香蕉-全能图片V1 应用合集_1963466085067739137.json、视频生成/图生视频/-全能图片V1 玩法合集_1971482222584905730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `EmptyImage`
- `Fast Groups Muter (rgthree)`
- `GeminiImageNode`
- `GetImageSize`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImagePadForOutpaintMasked_UTK`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImageTextOverlay`
- `Int`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `TTP_text_mix`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `JanusImageUnderstanding` —— 1/2 个有
- `JanusModelLoader` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SDVN Any Show` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
