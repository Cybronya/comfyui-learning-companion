---
name: image_to_image_lora_sampler_unet_150
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9474
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1968953423150399489.json, 图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1970349247147241473.json, 图片生成/图生图/Qwen_产品多视角分镜场景_2017587044259733505.json, 图片生成/图生图/qwen-image-edit2511单图编辑--标准版--（必收藏）_2048729771428810754.json, 图片生成/图生图/位置偏移解决方案-Qwen-Image-Edit_1968671815499436033.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1968953423150399489.json、图片生成/图生图/Qwen-Image-Edit实现编辑图片的一致性_1970349247147241473.json、图片生成/图生图/Qwen_产品多视角分镜场景_2017587044259733505.json、图片生成/图生图/qwen-image-edit2511单图编辑--标准版--（必收藏）_2048729771428810754.json、图片生成/图生图/位置偏移解决方案-Qwen-Image-Edit_1968671815499436033.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ImageStitch` —— 3/5 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 3/5 个有
- `GroupSwitcher` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `Text` —— 2/5 个有
- `easy float` —— 2/5 个有
- `easy int` —— 2/5 个有
- `ImageScaleDownToSize` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
