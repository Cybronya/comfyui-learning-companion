---
name: text_to_image_upscale_lora_sampler_11
type: Text To Image
frequency: 3
level: strong
coverage: 0.749
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImpactInt, JjkText, JoinStrings, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy imageConcat]
members: [图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json, 图片生成/图生图/2106070948993654785.json, 图片生成/图生图/2106072614019096578.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json、图片生成/图生图/2106070948993654785.json、图片生成/图生图/2106072614019096578.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactInt`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、easy imageConcat
