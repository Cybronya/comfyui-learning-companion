---
name: text_to_image_lora_sampler_clip_200
type: Text To Image
frequency: 9
level: strong
coverage: 0.904556
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键OK老照片修复｜老孙AI图生图高清翻新还原_2088764893104267265.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093452133847883778.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093880576225927169.json, 图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093902874857263105.json, 图片生成/图生图/产品精修渲染放大V4.1｜Ai图生图高清处理_2093785737798967298.json, 图片生成/图生图/动漫到真人转换工作流｜图生图真人化写实转换_2106993877558317058.json, 图片生成/图生图/老照片修复多功能｜去水印偏色曝光一键处理_2089367623166414850.json, 图片生成/图生图/老照片翻新上色｜Flux2_Klein修复破损划痕校正颜色_2093499002330374146.json, 图片生成/图生图/老照片翻新上色｜Flux2_Klein修复破损划痕校正颜色_2093538882343235586.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_200

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/一键OK老照片修复｜老孙AI图生图高清翻新还原_2088764893104267265.json、图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093452133847883778.json、图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093880576225927169.json、图片生成/图生图/产品精修渲染放大V4.1｜AI商品图生图高清精修_2093902874857263105.json、图片生成/图生图/产品精修渲染放大V4.1｜Ai图生图高清处理_2093785737798967298.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
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
- `Flux2Scheduler` —— 5/9 个有
- `KSamplerSelect` —— 5/9 个有
- `孤海注释` —— 5/9 个有
- `ConstrainImage|pysssss` —— 4/9 个有
- `ImageScaleBy` —— 4/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `SeedVR2LoadDiTModel` —— 4/9 个有
- `SeedVR2LoadVAEModel` —— 4/9 个有
- `SeedVR2VideoUpscaler` —— 4/9 个有
- `Float` —— 3/9 个有
- `easy getNode` —— 3/9 个有
- `easy setNode` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `easy promptConcat` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
