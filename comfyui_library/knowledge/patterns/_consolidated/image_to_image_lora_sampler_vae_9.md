---
name: image_to_image_lora_sampler_vae_9
type: Image To Image
frequency: 8
level: strong
coverage: 0.842
common_nodes: [CFGNorm, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2509-批量测试_2001951383052009474.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2031922726943854593.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2034195279104184321.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2034202489414750209.json, 图片生成/图生图/Qwen-Edit-2511 风格迁移_2058000912211337217.json, 图片生成/图生图/QwenEdit2509服装白底图提取_1993628856821235713.json, 图片生成/图生图/【电商版】2509-LORA万能背景增加人物流_1985936658019299330.json, 图片生成/图生图/高斯泼溅指定旋转角度【适合电商场景_产品】_2014492335744225281.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/2509-批量测试_2001951383052009474.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2031922726943854593.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2034195279104184321.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2034202489414750209.json、图片生成/图生图/Qwen-Edit-2511 风格迁移_2058000912211337217.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `CR Seed` —— 5/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/8 个有
- `ImageStitch` —— 4/8 个有
- `CR Text` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `easy imageSize` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LoadDiffusionModelShared //Inspire` —— 1/8 个有
- `LoadSharpModel` —— 1/8 个有
- `LoadTextEncoderShared //Inspire` —— 1/8 个有
- `SharpPredict` —— 1/8 个有
- `YCGaussianPreview` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
