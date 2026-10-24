---
name: text_to_image_lora_sampler_clip_256
type: Text To Image
frequency: 7
level: strong
coverage: 0.914571
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LLaDA Image Base图像编辑 一句话改图方案_2108973949999730689.json, 图片生成/图生图/一键生成角色四视图｜Klein9b图生图角色设计_2090856279853064194.json, 图片生成/图生图/动漫少女现实化图生图｜二次元美少女写实还原_2106995350576910337.json, 图片生成/图生图/双图编辑｜Flux2-klein人像写真物品摄影，融合出新图_2099891317936574465.json, 图片生成/图生图/效果图洗图增强细节工作流｜AI渲染秒变真实感照片级_2103739286116986881.json, 图片生成/图生图/超强一致性全能编辑｜Flux2+Klein9b换装换背景_2092943005975146497.json, 视频生成/图生视频/Flux2Klein多图编辑9B加速版｜换脸换装都顺手｜图生视频前处理首选_2102632847407407106.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_256

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LLaDA Image Base图像编辑 一句话改图方案_2108973949999730689.json、图片生成/图生图/一键生成角色四视图｜Klein9b图生图角色设计_2090856279853064194.json、图片生成/图生图/动漫少女现实化图生图｜二次元美少女写实还原_2106995350576910337.json、图片生成/图生图/双图编辑｜Flux2-klein人像写真物品摄影，融合出新图_2099891317936574465.json、图片生成/图生图/效果图洗图增强细节工作流｜AI渲染秒变真实感照片级_2103739286116986881.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `VAEEncode` —— 6/7 个有
- `Flux2Scheduler` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `FluxKontextImageScale` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `Int` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `BasicScheduler` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `T8LLaDAImageCheckpointLoader` —— 1/7 个有
- `T8LLaDAImageEditConditioning` —— 1/7 个有
- `T8LLaDAImageScheduler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
