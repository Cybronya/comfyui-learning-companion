---
name: image_to_image_sampler_unet_vae_9
type: Image To Image
frequency: 13
level: moderate
coverage: 0.894462
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json, 图片生成/图生图/FireRed-Image-Edit工作流_2026563265744080898.json, 图片生成/图生图/Qwen image edit 2511 可视化灯光调节_2013071030331383810.json, 图片生成/图生图/Qwen-Edit-2511 可视化重打光（lora强化版)_2012421686733312002.json, 图片生成/图生图/一键氛围打光_2011310291442733057.json, 图片生成/图生图/可视化灯光调节(重打光lora强化版)_2021046893047980033.json, 图片生成/图生图/图像人物重新打光电商商品打精修千问模型plus_2077283170759827458.json, 图片生成/图生图/图像重打光 Qwen2511_2036012882982346753.json, 图片生成/图生图/图像重打光 Qwen2511_2076938070133395457.json, 图片生成/图生图/图像重打光_Qwen2511_2083573156970852354.json, 图片生成/图生图/图像重打光_Qwen2511_2095782087520514050.json, 图片生成/图生图/图像重打光_Qwen2511_2096073652218449921.json, 图片生成/图生图/🦖2511可视化重打灯光_2011613758954676226.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json、图片生成/图生图/FireRed-Image-Edit工作流_2026563265744080898.json、图片生成/图生图/Qwen image edit 2511 可视化灯光调节_2013071030331383810.json、图片生成/图生图/Qwen-Edit-2511 可视化重打光（lora强化版)_2012421686733312002.json、图片生成/图生图/一键氛围打光_2011310291442733057.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `EmptySD3LatentImage` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `QwenMultiangleLightningNode` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `ImageScaleToTotalPixels` —— 10/13 个有
- `AddLabel` —— 1/13 个有
- `CLIPTextEncode` —— 1/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有
- `Seed (rgthree)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 12 | 13 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 12，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
