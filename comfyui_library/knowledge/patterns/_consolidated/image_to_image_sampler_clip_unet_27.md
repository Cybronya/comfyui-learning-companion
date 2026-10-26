---
name: image_to_image_sampler_clip_unet_27
type: Image To Image
frequency: 11
level: strong
coverage: 0.943727
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHHiddenNodes, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/kontext精修   金属类产品   一键自动修图+放大_2059160218495447042.json, 图片生成/图生图/kontext精修 - 金属类产品 - 一键自动修图_2082349692842766338.json, 图片生成/图生图/kontext精修 金属类产品 一键自动修图_2080936033201508353.json, 图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2096789742024220673.json, 图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2097133761417801729.json, 图片生成/图生图/kontext精修_金属类产品_一键自动修图_2093236238542270466.json, 图片生成/图生图/kontext精修_金属类产品_一键自动修图_2093507488636293121.json, 图片生成/图生图/kontext精修一键自动修图 - 金属类产品_2053327010658824194.json, 图片生成/图生图/kontext精修金属类产品一键自动修图生成器_2060320852012527617.json, 图片生成/图生图/电商精修 - 金属类产品 - 一键自动修图_2112023408560136194.json, 图片生成/图生图/阿清的kontext产品精修_2082345306645164034.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/kontext精修   金属类产品   一键自动修图+放大_2059160218495447042.json、图片生成/图生图/kontext精修 - 金属类产品 - 一键自动修图_2082349692842766338.json、图片生成/图生图/kontext精修 金属类产品 一键自动修图_2080936033201508353.json、图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2096789742024220673.json、图片生成/图生图/kontext精修_-_金属类产品_-_一键自动修图_2097133761417801729.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/11 个有
- `SeedVR2LoadDiTModel` —— 1/11 个有
- `SeedVR2LoadVAEModel` —— 1/11 个有
- `SeedVR2VideoUpscaler` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
