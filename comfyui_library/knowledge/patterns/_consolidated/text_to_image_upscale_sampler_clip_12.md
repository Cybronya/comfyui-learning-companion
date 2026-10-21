---
name: text_to_image_upscale_sampler_clip_12
type: Text To Image
frequency: 5
level: weak
coverage: 0.7418
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy imageConcat]
members: [图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json, 图片生成/图生图/2106070948993654785.json, 图片生成/图生图/2106072614019096578.json, 图片生成/文生图/Z-IMAGE：文生图、自动反推洗图_1995339189359140866.json, 图片生成/文生图/Z-image 宇宙超级无敌洗图_1995299863191597058.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json、图片生成/图生图/2106070948993654785.json、图片生成/图生图/2106072614019096578.json、图片生成/文生图/Z-IMAGE：文生图、自动反推洗图_1995339189359140866.json、图片生成/文生图/Z-image 宇宙超级无敌洗图_1995299863191597058.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `JoinStrings` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_Translator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 5 | 54% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 45% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 68% |
| 宽度 | 80 | 80 - 1920 | 5 | 0% |
| 高度 | 80 | 80 - 1920 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 宽度 中位数 80，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 0%
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、easy imageConcat
