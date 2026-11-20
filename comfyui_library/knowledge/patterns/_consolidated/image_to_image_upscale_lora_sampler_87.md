---
name: image_to_image_upscale_lora_sampler_87
type: Image To Image
frequency: 3
level: strong
coverage: 0.878667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, EmptyFlux2LatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/溶图打光-F.2 Klein人像细节迁移+高清放大_2095354701352095746.json, 平台全量/电商产品精修 服饰箱包化妆品去瑕疵  深度优化版 照片精修 更好的纹理保留 SeedVR2 内附高清_2045004913238872065.json, 平台全量/电商产品精修 服饰箱包化妆品去瑕疵 SeedVR2 高清放大功能 深度优化版 照片精修 更好的纹理保_2044979858266132482.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/溶图打光-F.2 Klein人像细节迁移+高清放大_2095354701352095746.json、平台全量/电商产品精修 服饰箱包化妆品去瑕疵  深度优化版 照片精修 更好的纹理保留 SeedVR2 内附高清_2045004913238872065.json、平台全量/电商产品精修 服饰箱包化妆品去瑕疵 SeedVR2 高清放大功能 深度优化版 照片精修 更好的纹理保_2044979858266132482.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `HYPIRAdvancedRestoration` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `ImageScaleBy` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
