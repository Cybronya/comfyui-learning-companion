---
name: image_to_image_sampler_clip_unet_9
type: Image To Image
frequency: 21
level: strong
coverage: 0.933667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext精修   金属类产品   一键自动修图+放大_2059160218495447042.json, 图片生成/图生图/kontext精修 - 金属类产品 - 一键自动修图_2082349692842766338.json, 图片生成/图生图/kontext精修 金属类产品 一键自动修图_2080936033201508353.json, 图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2096789742024220673.json, 图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2097133761417801729.json, 图片生成/图生图/kontext精修_金属类产品_一键自动修图_2093236238542270466.json, 图片生成/图生图/kontext精修_金属类产品_一键自动修图_2093507488636293121.json, 图片生成/图生图/kontext精修一键自动修图 - 金属类产品_2053327010658824194.json, 图片生成/图生图/kontext精修金属类产品一键自动修图生成器_2060320852012527617.json, 图片生成/图生图/室内-FLUX日景光影优化工作流_2044313078275248130.json, 图片生成/图生图/电商精修 - 金属类产品 - 一键自动修图_2112023408560136194.json, 图片生成/图生图/阿清的kontext产品精修_2082345306645164034.json, 平台全量/kontext电商产品一键修图自动磨皮工作流_1955103054115717122.json, 平台全量/kontext精修 - 金属类产品 - 一键自动修图_1947533027837644802.json, 平台全量/kontext精修 - 金属类产品 - 小梅V3_1979106500239069185.json, 平台全量/kontext精修 - 金属类产品 自动修图_2034079617866272770.json, 平台全量/kontext精修 _ 金属类产品 _ 一键自动修图生成器_2052236590101082114.json, 平台全量/kontext自动精修 - 金属类产品_2071625793779879938.json, 平台全量/一键自动修图_2108826470603907074.json, 平台全量/人物场景光影融合_1996434538677026818.json, 平台全量/室内日景光影优化_1999815286259937282.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/kontext精修   金属类产品   一键自动修图+放大_2059160218495447042.json、图片生成/图生图/kontext精修 - 金属类产品 - 一键自动修图_2082349692842766338.json、图片生成/图生图/kontext精修 金属类产品 一键自动修图_2080936033201508353.json、图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2096789742024220673.json、图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2097133761417801729.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageMaskScaleAs` —— 18/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/21 个有
- `RHHiddenNodes` —— 18/21 个有
- `easy imageConcat` —— 18/21 个有
- `easy imageSize` —— 18/21 个有
- `easy int` —— 18/21 个有
- `ImageScaleBy` —— 4/21 个有
- `SeedVR2LoadDiTModel` —— 4/21 个有
- `SeedVR2LoadVAEModel` —— 4/21 个有
- `SeedVR2VideoUpscaler` —— 4/21 个有
- `ConditioningZeroOut` —— 3/21 个有
- `FluxKontextImageScale` —— 3/21 个有
- `LoraLoaderModelOnly` —— 3/21 个有
- `LayerUtility: PurgeVRAM V2` —— 2/21 个有
- `FaceDetailer` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `UltralyticsDetectorProvider` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 21 | 86% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 1 | 21 | 96% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，21 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 1，21 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
