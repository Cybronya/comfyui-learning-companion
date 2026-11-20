---
name: unknown_workflow_generic_312
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.4995
common_nodes: [CM_IntUnaryOperation, GetImageSizeAndCount, GetNode, ImageBatchMulti, ImageLoader, ImageScaleToTotalPixels, MemoryCleaner, PreviewImage, Qwen3VL_Advanced, RH_LLMAPI_NODE, SaveImage, SetNode, SimpleMath+, StringFunction|pysssss, easy anythingIndexSwitch, easy anythingInversedSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片 pro_2006302920123355137.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片2_2062216759503052802.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片2_2066055875628167168.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2062203582530801665.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 2.0_2066055876622217216.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片_2006195630225498113.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_312

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-全能图片G- Image 2.0_2085944675277557762.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片 pro_2006302920123355137.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片2_2062216759503052802.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片2_2066055875628167168.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-全能图片G- Image 1.5_2008194109030277121.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 8 个 workflow 都包含：
- `CM_IntUnaryOperation`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchMulti`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `MemoryCleaner`
- `PreviewImage`
- `Qwen3VL_Advanced`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `StringFunction|pysssss`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 7/8 个有
- `ImageConcanate` —— 5/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `RH_RhartImageG2ImageToImage` —— 3/8 个有
- `RH_RhartImageNG31FlashImageToImage` —— 2/8 个有
- `RH_GPT_Image15` —— 1/8 个有
- `RH_Nano_Banana2_Image2Image` —— 1/8 个有
- `RH_Nano_Banana_Image2Image` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
