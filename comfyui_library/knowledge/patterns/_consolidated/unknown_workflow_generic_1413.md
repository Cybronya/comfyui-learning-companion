---
name: unknown_workflow_generic_1413
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7195
common_nodes: [Bjornulf_ShowInt, GH_MaskCropV2, GetNode, GoohaiUniversalSlider, LoadImage, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, SetNode, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: []
missing: []
members: [图片生成/图生图/lora制作 _ 裁剪+主体白模 _ for循环 zip批量_2102296238237503490.json, 图片生成/图生图/批量裁剪面部 1：1_2104751652443086849.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1413

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/lora制作 _ 裁剪+主体白模 _ for循环 zip批量_2102296238237503490.json、图片生成/图生图/批量裁剪面部 1：1_2104751652443086849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `GH_MaskCropV2`
- `GetNode`
- `GoohaiUniversalSlider`
- `LoadImage`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `SetNode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
