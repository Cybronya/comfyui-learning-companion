---
name: unknown_workflow_generic_1954
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [CR Prompt Text, Comfly_api_set, Comfly_gpt_image_2_official_ratio, ImageTile+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, easy imageSizeBySide, easy showAnything]
problems: []
missing: []
members: [平台全量/宠物表情包_2054444561199583233.json, 平台全量/最美证件照PRO_2054444607311753217.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1954

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/宠物表情包_2054444561199583233.json、平台全量/最美证件照PRO_2054444607311753217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_api_set`
- `Comfly_gpt_image_2_official_ratio`
- `ImageTile+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `easy imageSizeBySide`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR String To Number` —— 1/2 个有
- `Comfly_gpt_image_2_fal` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImpactStringSelector` —— 1/2 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
