---
name: unknown_workflow_generic_1452
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7885
common_nodes: [CR Prompt Text, DF_Integer, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, RHHiddenNodes, RH_RhartImageG2OfficialImageToImage, RH_RhartImageG2TextToImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs]
problems: []
missing: []
members: [图片生成/图生图/全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json, 图片生成/文生图/全能G2-Images 2.0文生图+八张图文生图工作流_2058924668106657794.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1452

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json、图片生成/文生图/全能G2-Images 2.0文生图+八张图文生图工作流_2058924668106657794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `DF_Integer`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `RHHiddenNodes`
- `RH_RhartImageG2OfficialImageToImage`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
