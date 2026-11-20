---
name: unknown_workflow_generic_1975
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8435
common_nodes: [CR Prompt Text, Comfly_api_set, Comfly_gpt_image_2_official_ratio, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, easy imageSizeBySide, easy showAnything]
problems: []
missing: []
members: [平台全量/老照片修复_2054444576013864962.json, 平台全量/领英形象照_2054444592216453122.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1975

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/老照片修复_2054444576013864962.json、平台全量/领英形象照_2054444592216453122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_api_set`
- `Comfly_gpt_image_2_official_ratio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `easy imageSizeBySide`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Comfly_gpt_image_2_fal` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
