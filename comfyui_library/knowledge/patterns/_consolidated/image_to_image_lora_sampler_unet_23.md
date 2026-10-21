---
name: image_to_image_lora_sampler_unet_23
type: Image To Image
frequency: 4
level: strong
coverage: 0.8705
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy loraStack, easy loraStackApply, String Literal, easy seed]
members: [图片生成/图生图/2019387229856075777.json, 图片生成/图生图/2081382750556348418.json, 图片生成/图生图/2081650003457691649.json, 图片生成/文生图/1958888407248351234.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2019387229856075777.json、图片生成/图生图/2081382750556348418.json、图片生成/图生图/2081650003457691649.json、图片生成/文生图/1958888407248351234.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2EditGroundedEncode` —— 3/4 个有
- `Krea2EditModelPatch` —— 3/4 个有
- `String Literal` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ColorMatchV2` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `easy loraStack` —— 1/4 个有
- `easy loraStackApply` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy loraStack、easy loraStackApply、String Literal、easy seed
