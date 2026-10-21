---
name: text_to_image_lora_sampler_clip_272
type: Text To Image
frequency: 4
level: strong
coverage: 0.821
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, EmptyMiniMaxH3LatentAV, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageFromBatch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PreviewImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, ScheduledCFGGuidance, UNETLoader, VAEDecode, VAELoader, easy MiniMaxH3ReferenceToVideoBridge, easy imageColorMatch, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMaxH3图像编辑文生图｜高一致性真实感生成_2094851558113628161.json, 数字人/数字人/更真实一致性升级｜MiniMaxH3图像编辑文生图生成_2095047981555867650.json, 数字人/数字人/海螺H3图像编辑+文生图｜高还原度双模式生成_2094850066522664962.json, 数字人/数字人/高还原度文生图图像编辑｜海螺 H3数字人图生图_2095046448059609089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_272

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/MiniMaxH3图像编辑文生图｜高一致性真实感生成_2094851558113628161.json、数字人/数字人/更真实一致性升级｜MiniMaxH3图像编辑文生图生成_2095047981555867650.json、数字人/数字人/海螺H3图像编辑+文生图｜高还原度双模式生成_2094850066522664962.json、数字人/数字人/高还原度文生图图像编辑｜海螺 H3数字人图生图_2095046448059609089.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyMiniMaxH3LatentAV`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ScheduledCFGGuidance`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy imageColorMatch`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
