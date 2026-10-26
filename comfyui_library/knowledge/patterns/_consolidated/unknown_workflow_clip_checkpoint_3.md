---
name: unknown_workflow_clip_checkpoint_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, GetImageSize+, Image Repeat Tile To Size, ImageCompositeMasked, ImageScale, Int, LoadImage, MathExpression|pysssss, RHHiddenNodes, RH_RhartImageG2ImageToImage, SAM3_Detect, SaveImage, ShowText|pysssss, TextGenerate, YCMaskBlur, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/调整印花大小工作流5月28日_2060261853200207873.json, 图片生成/图生图/调整印花大小工作流5月28日_2060271870632615937.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/调整印花大小工作流5月28日_2060261853200207873.json、图片生成/图生图/调整印花大小工作流5月28日_2060271870632615937.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageSize+`
- `Image Repeat Tile To Size`
- `ImageCompositeMasked`
- `ImageScale`
- `Int`
- `LoadImage`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `RH_RhartImageG2ImageToImage`
- `SAM3_Detect`
- `SaveImage`
- `ShowText|pysssss`
- `TextGenerate`
- `YCMaskBlur`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
