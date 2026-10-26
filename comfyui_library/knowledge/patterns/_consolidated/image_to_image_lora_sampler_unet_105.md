---
name: image_to_image_lora_sampler_unet_105
type: Image To Image
frequency: 6
level: moderate
coverage: 0.875667
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json, 图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json, 图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json, 图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json, 图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json, 图片生成/图生图/🥨Qwen 白底换背景 电商换背景🥨_1986265387476144129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_105

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json、图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json、图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json、图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json、图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `StringFunction|pysssss` —— 4/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `ImpactInt` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `easy imageRemBg` —— 3/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PIP_图像联结` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `String` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 6 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 68% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，6 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
