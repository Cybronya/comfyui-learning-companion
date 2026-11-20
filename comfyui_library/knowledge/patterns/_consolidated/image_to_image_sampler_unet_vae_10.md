---
name: image_to_image_sampler_unet_vae_10
type: Image To Image
frequency: 14
level: moderate
coverage: 0.908643
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen去水印_1986102218543824897.json, 图片生成/图生图/Z image 图生图（洗图）_1993888000021037058.json, 图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json, 图片生成/图生图/Z-Image-Turbo-人像去Ai味真实质感_1994013061161959425.json, 图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json, 图片生成/图生图/Z-Image图生图洗图_2094304765537771521.json, 图片生成/图生图/Z-Image图生图洗图_2101937229131243521.json, 图片生成/图生图/Z-Image图生图洗图_2105121490088841217.json, 图片生成/图生图/Z-Image图生图洗图_2105498770577387521.json, 图片生成/图生图/Z-Image图生图洗图_2112490094929203201.json, 图片生成/图生图/Z-Image图生图洗图_2116317816407285762.json, 图片生成/图生图/Z-image + LoRA 图生图工作流_2059600757091033090.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2059610100196798465.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2091491515486003202.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen去水印_1986102218543824897.json、图片生成/图生图/Z image 图生图（洗图）_1993888000021037058.json、图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json、图片生成/图生图/Z-Image-Turbo-人像去Ai味真实质感_1994013061161959425.json、图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 13/14 个有
- `Image Comparer (rgthree)` —— 13/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/14 个有
- `ConditioningZeroOut` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `RepeatLatentBatch` —— 3/14 个有
- `AIO_Preprocessor` —— 2/14 个有
- `ModelPatchLoader` —— 2/14 个有
- `ZImageFunControlnet` —— 2/14 个有
- `ImageResize+` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 14 | 83% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 1.5 | 14 | 80% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 0.85 | 0.19 - 1 | 14 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，14 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 1.5，14 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 0.85，观测区间 0.19 - 1，14 个样本
- 高发问题（10/14 个样本）：Steps较低可能导致细节不足
