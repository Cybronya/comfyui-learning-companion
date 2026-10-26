---
name: unknown_workflow_clip_checkpoint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7825
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DrawBBoxes, GetImageSize, LayerUtility: ColorImage, LayerUtility: ImageBlend V2, LoadImage, MaskPreview, MaskToImage, PreviewImage, SAM3_Detect, SaveImage, Text]
problems: []
missing: []
members: [图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json, 图片生成/图生图/sam3.1目标检测_2112924412260478977.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json、图片生成/图生图/sam3.1目标检测_2112924412260478977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DrawBBoxes`
- `GetImageSize`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlend V2`
- `LoadImage`
- `MaskPreview`
- `MaskToImage`
- `PreviewImage`
- `SAM3_Detect`
- `SaveImage`
- `Text`

**可变部分**（部分 workflow 才有）：
- `CreateBoundingBoxes` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
