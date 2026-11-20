---
name: image_to_image_lora_sampler_clip_5
type: Image To Image
frequency: 20
level: strong
coverage: 0.8657
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json, 图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json, 图片生成/图生图/flux-2-klein服装精修衣服去皱版型整理_2048397208462041090.json, 图片生成/图生图/flux2klein服装精修衣服去皱版型整理_2050843092210728962.json, 图片生成/图生图/服装精修_2094649653454270466.json, 图片生成/图生图/服装精修去褶皱_版型整理_2037345299408097281.json, 图片生成/图生图/服装精修图生图去褶皱去皱纹_2065870420028518401.json, 图片生成/图生图/模特服装版型调整美化穿着优化精修去褶皱_2065292480492425217.json, 图片生成/图生图/精修美化电商产品图片_2070330390862192641.json, 图片生成/图生图/老孙AI  去除褶皱  服装精修_2088885891363336194.json, 图片生成/图生图/首饰_珠宝_2056753455921975297.json, 图片生成/图生图/首饰草图转换首饰草图转换V1.0_2094360265574928385.json, 图片生成/文生图/空白工作流_2088539683264483329.json, 平台全量/F.2klein服装精修衣服去皱版型整理_2058216111321214978.json, 平台全量/F2klein9B-服装精修-去背景-生成白底图_2040834889058095106.json, 平台全量/hu精修_2070771329116229634.json, 平台全量/万能产品修图 精修首饰_珠宝  Flux-2-Klein-9B 抠图png透明图 五金数码珠宝箱包_2038418447725498369.json, 平台全量/产品修图+4k放大_2087026469066334210.json, 平台全量/产品精修_2047240512008101890.json, 平台全量/批量抠图+换背景+精修_2052363626610216961.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/F.2Kiein全类目产品精修真实感全类目_2103098660434305026.json、图片生成/图生图/F.2klein服装精修衣服去皱版型整理_2058031272836026370.json、图片生成/图生图/flux-2-klein服装精修衣服去皱版型整理_2048397208462041090.json、图片生成/图生图/flux2klein服装精修衣服去皱版型整理_2050843092210728962.json、图片生成/图生图/服装精修_2094649653454270466.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 19/20 个有
- `JjkText` —— 19/20 个有
- `FluxGuidance` —— 18/20 个有
- `easy promptConcat` —— 18/20 个有
- `Float` —— 17/20 个有
- `EmptyFlux2LatentImage` —— 14/20 个有
- `ImpactInt` —— 13/20 个有
- `Int` —— 5/20 个有
- `Fast Groups Bypasser (rgthree)` —— 4/20 个有
- `GrowMask` —— 4/20 个有
- `InvertMask` —— 4/20 个有
- `JoinImageWithAlpha` —— 4/20 个有
- `LayerMask: BiRefNetUltraV2` —— 3/20 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/20 个有
- `TT_img_enc` —— 2/20 个有
- `BiRefNetRMBG` —— 1/20 个有
- `HAIGC_SaveImagesToZip` —— 1/20 个有
- `Image Save` —— 1/20 个有
- `ImageUpscaleWithModel` —— 1/20 个有
- `Load Image Batch` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `RHUploadZip_V2` —— 1/20 个有
- `UpscaleModelLoader` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（26/20 个样本）：Steps较低可能导致细节不足
