---
name: image_to_image_lora_sampler_unet_142
type: Image To Image
frequency: 5
level: strong
coverage: 0.9814
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageResizeKJv2, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/生图-一键四视图白底图-Krea2_2097677926920712194.json, 图片生成/图生图/角色四视图辅助生成_2096880673448615937.json, 图片生成/文生图/krea2-人物四视图_2094627103068217345.json, 数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json, 数字人/数字人/多面部参考融合生成人物四视图_2098589358654844929.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_142

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/生图-一键四视图白底图-Krea2_2097677926920712194.json、图片生成/图生图/角色四视图辅助生成_2096880673448615937.json、图片生成/文生图/krea2-人物四视图_2094627103068217345.json、数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json、数字人/数字人/多面部参考融合生成人物四视图_2098589358654844929.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
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
- `Label (rgthree)` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `easy positive` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
