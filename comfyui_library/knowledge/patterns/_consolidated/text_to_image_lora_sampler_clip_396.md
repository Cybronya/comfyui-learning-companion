---
name: text_to_image_lora_sampler_clip_396
type: Text To Image
frequency: 5
level: strong
coverage: 0.8138
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, ImageFromBatch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/保持人物一致性图像编辑图生图｜MiniMax-H3场景图片编辑工作流_2087206051509792770.json, 数字人/数字人/MiniMaxH3图像编辑文生图｜高一致性真实感生成_2094851558113628161.json, 数字人/数字人/更真实一致性升级｜MiniMaxH3图像编辑文生图生成_2095047981555867650.json, 数字人/数字人/海螺H3图像编辑+文生图｜高还原度双模式生成_2094850066522664962.json, 数字人/数字人/高还原度文生图图像编辑｜海螺 H3数字人图生图_2095046448059609089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_396

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/保持人物一致性图像编辑图生图｜MiniMax-H3场景图片编辑工作流_2087206051509792770.json、数字人/数字人/MiniMaxH3图像编辑文生图｜高一致性真实感生成_2094851558113628161.json、数字人/数字人/更真实一致性升级｜MiniMaxH3图像编辑文生图生成_2095047981555867650.json、数字人/数字人/海螺H3图像编辑+文生图｜高还原度双模式生成_2094850066522664962.json、数字人/数字人/高还原度文生图图像编辑｜海螺 H3数字人图生图_2095046448059609089.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 4/5 个有
- `CR Text` —— 4/5 个有
- `EmptyMiniMaxH3LatentAV` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `MiniMaxH3BlockCacheT8` —— 4/5 个有
- `MiniMaxH3ImageToVideo` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LayerUtility: SaveImagePlus` —— 1/5 个有
- `MiniMaxH3ReferenceToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
