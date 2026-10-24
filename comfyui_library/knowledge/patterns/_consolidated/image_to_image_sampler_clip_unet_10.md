---
name: image_to_image_sampler_clip_unet_10
type: Image To Image
frequency: 18
level: moderate
coverage: 0.898111
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/55.tonnie-flux2编辑图像_2008311211066138626.json, 图片生成/图生图/F.2 klein9B工业级产品精修_2054118658212941825.json, 图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json, 图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json, 图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json, 图片生成/图生图/Flux 2-klein9B工业级产品精修_2015804302496899073.json, 图片生成/图生图/Flux+2-klein9B工业级产品精修_2040782267097812993.json, 图片生成/图生图/WH-AI-Studio（产品精修、旧变新）（人物服装提取、去皱褶）（人物、产品去AI感）电商三合一_2022679693748604930.json, 图片生成/图生图/flux-2-klein服装精修衣服去皱版型整理_2048397208462041090.json, 图片生成/图生图/flux2klein服装精修衣服去皱版型整理_2050843092210728962.json, 图片生成/图生图/工业级产品精修Flux2-klein_2018881806765920258.json, 图片生成/图生图/服装精修_2094649653454270466.json, 图片生成/图生图/服装精修去褶皱_版型整理_2037345299408097281.json, 图片生成/图生图/服装精修图生图去褶皱去皱纹_2065870420028518401.json, 图片生成/图生图/模特服装版型调整美化穿着优化精修去褶皱_2065292480492425217.json, 图片生成/图生图/精修美化电商产品图片_2070330390862192641.json, 图片生成/图生图/老孙AI  去除褶皱  服装精修_2088885891363336194.json, 图片生成/图生图/首饰_珠宝_2056753455921975297.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/55.tonnie-flux2编辑图像_2008311211066138626.json、图片生成/图生图/F.2 klein9B工业级产品精修_2054118658212941825.json、图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json、图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json、图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `LoraLoaderModelOnly` —— 17/18 个有
- `Image Comparer (rgthree)` —— 16/18 个有
- `EmptyFlux2LatentImage` —— 14/18 个有
- `Float` —— 13/18 个有
- `FluxGuidance` —— 12/18 个有
- `Int` —— 10/18 个有
- `JjkText` —— 10/18 个有
- `easy promptConcat` —— 10/18 个有
- `CR Prompt Text` —— 6/18 个有
- `ImpactInt` —— 6/18 个有
- `TT_img_enc` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `GrowMask` —— 1/18 个有
- `InvertMask` —— 1/18 个有
- `JoinImageWithAlpha` —— 1/18 个有
- `LayerMask: BiRefNetUltraV2` —— 1/18 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/18 个有
- `ModelPatchTorchSettings` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有
- `Switch` —— 1/18 个有
- `easy imageConcat` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 18 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，18 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（16/18 个样本）：Steps较低可能导致细节不足
