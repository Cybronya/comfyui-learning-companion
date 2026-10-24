---
name: image_to_image_sampler_unet_vae_31
type: Image To Image
frequency: 8
level: moderate
coverage: 0.9135
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json, 图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json, 图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json, 图片生成/图生图/Qwen-Edit-2511 人物姿势模仿工作流_2091518524282990593.json, 图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json, 图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json, 图片生成/图生图/🥨Qwen 白底换背景 电商换背景🥨_1986265387476144129.json, 图片生成/文生图/workflow_2073294866825695233.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_31

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json、图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json、图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json、图片生成/图生图/Qwen-Edit-2511 人物姿势模仿工作流_2091518524282990593.json、图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `StringFunction|pysssss` —— 4/8 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/8 个有
- `DWPreprocessor` —— 3/8 个有
- `ImpactInt` —— 3/8 个有
- `easy imageRemBg` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `JWInteger` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 8 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 53% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，8 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
