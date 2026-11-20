---
name: unknown_workflow_sampler_unet_vae_222
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.805333
common_nodes: [CLIPLoader, ColorMatch, GrowMask, GrowMaskWithBlur, Image Crop Face, ImageCompositeMasked, ImageConcanate, ImageResize+, KSampler, LoadImage, PainterFluxImageEdit, PreviewImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FluxKlein人物场景迁移_2018511712462315521.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2015309931343253505.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2017974585118953473.json, 图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2021996290359431169.json, 平台全量/Flux2-Klein 姿势迁移 人物模特场景动作迁移  参考姿势一致性_2019969377239572481.json, 平台全量/万能姿势迁移 Flux2-Klein  人物模特场景动作迁移 参考姿势一致性_2020759703931854850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_222

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FluxKlein人物场景迁移_2018511712462315521.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2015309931343253505.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2017974585118953473.json、图片生成/图生图/FluxKlein人物场景迁移保持和参考姿势一致性_2021996290359431169.json、平台全量/Flux2-Klein 姿势迁移 人物模特场景动作迁移  参考姿势一致性_2019969377239572481.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Text` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `MaskPreview+` —— 5/6 个有
- `Text Concatenate` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `QwenVisionNode` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `JWStringMultiline` —— 1/6 个有
- `MaskPreview` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
