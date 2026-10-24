---
name: text_to_image_upscale_sampler_clip_4
type: Text To Image
frequency: 19
level: weak
coverage: 0.835579
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json, 图片生成/图生图/Qwen Image 2.1洗图完美版工作流，图生图去AI感处理工具_2106483588454772738.json, 图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json, 图片生成/图生图/Qwen3反推提示词_2050402437873315841.json, 图片生成/图生图/Z-Image去AI感工作流｜图片质感真实化处理生成_2096328592773959682.json, 图片生成/图生图/Z-Image去AI感精修｜图生图高清放大还原真实质感_2096249885086539777.json, 图片生成/图生图/Z_image反推洗图重绘去Ai感｜SeedVR高清放大对比生成_2095496814714773506.json, 图片生成/图生图/qwen-image-2.1洗图完美版｜图生图画质还原细节拉满_2106234956572876802.json, 图片生成/图生图/qwen3反推+qwen2.1洗图重绘去AI感｜SeedVR高清放大_2110721701603532801.json, 图片生成/图生图/qwen3反推Krea2洗图重绘去除Ai感加SeedVR放大 照片级质感优化_2109688382661152770.json, 图片生成/图生图/qwen3反推qwen2.1重绘洗图｜去AI感SeedVR放大写实_2110745964003815425.json, 图片生成/图生图/qwen3反推加qwen2.1洗图重绘，去Ai感加SeedVR放大_2111590246059167746.json, 图片生成/图生图/qwen3反推加qwen2.1洗图重绘，去Ai感加SeedVR高清放大_2110846136918568961.json, 图片生成/图生图/qwen3反推洗图重绘去Ai感｜Krea2+SeedVR高清放大_2095517646132432897.json, 图片生成/图生图/qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001.json, 图片生成/图生图/图片去AI感工作流｜Z_image反推洗图重绘+SeedVR放大_2095232629577699330.json, 图片生成/图生图/最强还原人物真实度去AI感｜图生图直出自然人像质感_2111297352739934210.json, 图片生成/文生图/Z-tmage高清文生图+反推提示词并生图_2056899865396989954.json, 图片生成/文生图/qwen3反推提示词并生图+Z-tmage高清文生图_2031245492893519874.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/反推提示词/Qwen3反推Krea2洗图重绘去除AI感加SeedVR放大，图生图高清修复方案_2106070948993654785.json、图片生成/图生图/Qwen Image 2.1洗图完美版工作流，图生图去AI感处理工具_2106483588454772738.json、图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json、图片生成/图生图/Qwen3反推提示词_2050402437873315841.json、图片生成/图生图/Z-Image去AI感工作流｜图片质感真实化处理生成_2096328592773959682.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 18/19 个有
- `PreviewImage` —— 17/19 个有
- `ImageScaleBy` —— 16/19 个有
- `JjkText` —— 16/19 个有
- `LayerUtility: PurgeVRAM` —— 16/19 个有
- `ShowText|pysssss` —— 16/19 个有
- `solarL_SaveImagesToZip` —— 16/19 个有
- `孤海注释` —— 16/19 个有
- `LayerUtility: ImageReel` —— 15/19 个有
- `LayerUtility: ImageReelComposit` —— 15/19 个有
- `easy imageConcat` —— 15/19 个有
- `CR Prompt List` —— 3/19 个有
- `Float` —— 3/19 个有
- `MemoryCleaner` —— 3/19 个有
- `Primitive integer [Crystools]` —— 3/19 个有
- `Text Multiline` —— 3/19 个有
- `SomethingToString` —— 2/19 个有
- `easy convertAnything` —— 2/19 个有
- `easy indexAnything` —— 2/19 个有
- `easy saveText` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `LoraLoader` —— 1/19 个有
- `ModelSamplingAuraFlow` —— 1/19 个有
- `MuyeTextEditOutput` —— 1/19 个有
- `easy textSwitch` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 19 | 58% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 19 | 68% |
| 采样算法 | er_sde | - | 19 | 84% |
| 调度器 | beta | - | 19 | 84% |
| 重绘幅度 | 1 | 0.7 - 1 | 19 | 93% |
| 宽度 | 80 | 80 - 1080 | 19 | 0% |
| 高度 | 80 | 80 - 1920 | 19 | 0% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，19 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，19 个样本
- 采样算法 最常用 er_sde，19 个样本，一致性 84%
- 调度器 最常用 beta，19 个样本，一致性 84%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，19 个样本，取值集中（一致性 93%）
- 宽度 中位数 80，观测区间 80 - 1080，19 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，19 个样本，取值分散，一致性仅 0%
- 高发问题（17/19 个样本）：Steps较低可能导致细节不足
