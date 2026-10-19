---
name: image_to_image_lora_sampler_unet_10
type: Image To Image
frequency: 4
level: strong
coverage: 0.9295
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102619986266251266.json, 数字人/数字人/Krea2 人物定妆照_2092034511797309441.json, 数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json, 数字人/数字人/多面部参考融合生成人物四视图_2098589358654844929.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2102619986266251266.json、数字人/数字人/Krea2 人物定妆照_2092034511797309441.json、数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json、数字人/数字人/多面部参考融合生成人物四视图_2098589358654844929.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 12 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 12，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
