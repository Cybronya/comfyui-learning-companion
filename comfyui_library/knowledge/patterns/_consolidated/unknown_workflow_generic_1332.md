---
name: unknown_workflow_generic_1332
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6555
common_nodes: [GetImageSize, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleDownToSize, LoadImage, PreviewImage, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, SaveImage, Text Multiline, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/-全能图片V1大香蕉模型双图非API调用版本V.1.0_1960637549888831490.json, 图片生成/图生图/全能图片V1谷歌大香蕉(单、双)图片编辑工作流_1960529318952710145.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1332

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/-全能图片V1大香蕉模型双图非API调用版本V.1.0_1960637549888831490.json、图片生成/图生图/全能图片V1谷歌大香蕉(单、双)图片编辑工作流_1960529318952710145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleDownToSize`
- `LoadImage`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `Text Multiline`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
