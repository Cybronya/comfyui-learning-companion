---
name: image_to_image_sampler_clip_unet_45
type: Image To Image
frequency: 8
level: moderate
coverage: 0.9455
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/CMF_2029777059152666625.json, 图片生成/图生图/FLUX 2 图生图_1993556092405874690.json, 图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json, 图片生成/图生图/flux.2-三图融合-标准版-（必收藏）_2052738645555200002.json, 图片生成/图生图/【楚心钟陌】klein极速动漫转真人_2015778697990643714.json, 图片生成/图生图/【遇见AI】longcat_image_基础文生图_2059112298840682497.json, 图片生成/图生图/模特_2029780558808621057.json, 图片生成/图生图/👽老许Gary：Klein局部编辑丨最实用的工作流_2046092909593763841.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_45

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/CMF_2029777059152666625.json、图片生成/图生图/FLUX 2 图生图_1993556092405874690.json、图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json、图片生成/图生图/flux.2-三图融合-标准版-（必收藏）_2052738645555200002.json、图片生成/图生图/【楚心钟陌】klein极速动漫转真人_2015778697990643714.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 5/8 个有
- `EmptyFlux2LatentImage` —— 4/8 个有
- `LayerUtility: ImageReel` —— 4/8 个有
- `LayerUtility: ImageReelComposit` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `RepeatLatentBatch` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `DrawMaskOnImage` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 8 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
