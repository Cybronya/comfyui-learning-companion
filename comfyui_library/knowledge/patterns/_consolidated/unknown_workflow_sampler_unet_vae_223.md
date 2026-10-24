---
name: unknown_workflow_sampler_unet_vae_223
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8
common_nodes: [CLIPLoader, ColorMatch, GrowMask, GrowMaskWithBlur, Image Crop Face, ImageCompositeMasked, ImageConcanate, ImageResize+, KSampler, LoadImage, PainterFluxImageEdit, PreviewImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FluxKlein人物场景迁移_2018511712462315521.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2015309931343253505.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2017974585118953473.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2021996290359431169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_223

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FluxKlein人物场景迁移_2018511712462315521.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2015309931343253505.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2017974585118953473.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2021996290359431169.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ColorMatch`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Crop Face`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `PainterFluxImageEdit`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `QwenVisionNode` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `JWStringMultiline` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（12/4 个样本）：Steps较低可能导致细节不足
