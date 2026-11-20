---
name: text_to_image_lora_sampler_clip_74
type: Text To Image
frequency: 15
level: strong
coverage: 0.907
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090574124233084930.json, 图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090887818322206722.json, 图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092078678518882305.json, 图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092617560872284161.json, 图片生成/图生图/一键生成角色四视图｜Klein9b图生图角色设计_2090856279853064194.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093452133847883778.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093880576225927169.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093902874857263105.json, 图片生成/图生图/产品精修渲染放大V4.1｜Ai图生图高清处理_2093785737798967298.json, 图片生成/图生图/动漫到真人转换工作流｜图生图真人化写实转换_2106993877558317058.json, 图片生成/图生图/动漫少女现实化图生图｜二次元美少女写实还原_2106995350576910337.json, 图片生成/图生图/双图编辑｜Flux2-klein人像写真物品摄影，融合出新图_2099891317936574465.json, 图片生成/图生图/图片风格迁移转化灵感造像师像素级保留与灵魂级风格注入生成器，图生图方案_2107600836317761538.json, 图片生成/图生图/灵感造像师图片风格迁移｜像素级保留画面灵魂级注入风格，图生图_2107316373348241410.json, 图片生成/图生图/灵感造像师风格迁移｜像素级保留加灵魂级风格注入二合一_2112857706112577537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090574124233084930.json、图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090887818322206722.json、图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092078678518882305.json、图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092617560872284161.json、图片生成/图生图/一键生成角色四视图｜Klein9b图生图角色设计_2090856279853064194.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Flux2Scheduler` —— 14/15 个有
- `ConditioningZeroOut` —— 13/15 个有
- `Image Comparer (rgthree)` —— 13/15 个有
- `孤海注释` —— 12/15 个有
- `GetImageSize` —— 11/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/15 个有
- `LayerUtility: ImageReel` —— 7/15 个有
- `LayerUtility: ImageReelComposit` —— 7/15 个有
- `ConstrainImage|pysssss` —— 4/15 个有
- `SegmentV2` —— 4/15 个有
- `easy imageColorMatch` —— 4/15 个有
- `CR Text Concatenate` —— 3/15 个有
- `ImageColorMatch+` —— 3/15 个有
- `PlaySound|pysssss` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `PreviewImage` —— 3/15 个有
- `Qwen3VL_Chat` —— 3/15 个有
- `easy imageConcat` —— 3/15 个有
- `PrimitiveInt` —— 2/15 个有
- `BasicScheduler` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `FluxKontextImageScale` —— 1/15 个有
- `ImageScaleToTotalPixels` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
