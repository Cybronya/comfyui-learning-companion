---
name: image_to_image_sampler_clip_unet_88
type: Image To Image
frequency: 5
level: strong
coverage: 0.906
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json, 图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json, 图片生成/图生图/Flux1-Kontext 生成手办_1970470030527897601.json, 图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json, 图片生成/图生图/Kontext Controlnet 合集（姿势，深度，线稿 一键切换）_1961646947767619586.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json、图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json、图片生成/图生图/Flux1-Kontext 生成手办_1970470030527897601.json、图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json、图片生成/图生图/Kontext Controlnet 合集（姿势，深度，线稿 一键切换）_1961646947767619586.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 4/5 个有
- `ControlNetLoader` —— 4/5 个有
- `FluxKontextImageScale` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `SetUnionControlNetType` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `EmptyLatentImage64` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `ShowText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 1.8 | 1.1 - 1.8 | 4 | 81% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.8，观测区间 1.1 - 1.8，4 个样本，取值集中（一致性 81%）
