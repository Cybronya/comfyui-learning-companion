---
name: unknown_workflow_sampler_unet_vae_123
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.812625
common_nodes: [AutoCropFaces, CLIPLoader, CR Text, DapaoImageAspectRatioResizeNode, Image Comparer (rgthree), ImageConcanate, KSampler, LoadImage, PainterFluxImageEdit, SaveImage, SolidMask, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy ifElse, easy imageRemBg, easy int, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/DG（整理)_Klein换脸 换头二合一 又快又好_2019256828802113537.json, 图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json, 图片生成/图生图/Flux2-Klein-精准换脸_换头_2016780019858673666.json, 图片生成/图生图/Flux2-Klein换脸&换头_2027726464363274241.json, 图片生成/图生图/Klein换脸+换头二合一_2025800867483488258.json, 图片生成/图生图/Klein换脸+换头二合一_2026595310755123202.json, 图片生成/图生图/MsPai换脸换头二合一_2057303632898514945.json, 图片生成/图生图/🤹Klein换脸 换头二合一 又快又好🤹_2016443125459324930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_123

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/DG（整理)_Klein换脸 换头二合一 又快又好_2019256828802113537.json、图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json、图片生成/图生图/Flux2-Klein-精准换脸_换头_2016780019858673666.json、图片生成/图生图/Flux2-Klein换脸&换头_2027726464363274241.json、图片生成/图生图/Klein换脸+换头二合一_2025800867483488258.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `CR Text`
- `DapaoImageAspectRatioResizeNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `PainterFluxImageEdit`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy ifElse`
- `easy imageRemBg`
- `easy int`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `easy sam3ImageSegmentation` —— 3/8 个有
- `easy sam3ModelLoader` —— 3/8 个有
- `AILab_MaskOverlay` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `Int` —— 1/8 个有
- `MaskPreview` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
