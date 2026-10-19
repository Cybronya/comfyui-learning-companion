---
name: unknown_workflow_generic_620
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [AIO_Preprocessor, Gemini3ImageNode, Gemini_Image_API, ImageBatchConcatNode, LoadImage, NanoBananaAIO, NanoBananaBatchProcessor, PreviewImage, RH_Nano_Banana2_Gemini31Flash, RH_Nano_Banana2_Gemini31Flash_Batch, SaveImage, Text]
problems: []
missing: []
members: [图片生成/图生图/2067507301606576129.json, 图片生成/图生图/Gemini-全能图片2-Preprocessor_2067507301606576129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_620

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2067507301606576129.json、图片生成/图生图/Gemini-全能图片2-Preprocessor_2067507301606576129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Gemini3ImageNode`
- `Gemini_Image_API`
- `ImageBatchConcatNode`
- `LoadImage`
- `NanoBananaAIO`
- `NanoBananaBatchProcessor`
- `PreviewImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_Nano_Banana2_Gemini31Flash_Batch`
- `SaveImage`
- `Text`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
