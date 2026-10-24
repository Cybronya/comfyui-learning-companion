---
name: image_to_image_lora_sampler_unet_119
type: Image To Image
frequency: 5
level: strong
coverage: 0.8898
common_nodes: [CFGNorm, CLIPLoader, Image Blank, ImageCompositeMasked, JoinImageWithAlpha, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/44.tonnie-Qwen Edit 2059修手_2004540574411751426.json, 图片生成/图生图/75.tonnie-2511万物精准移除_2011751771802181633.json, 图片生成/图生图/Qwen-edit-2511-万物精准移除_2009156898662129666.json, 图片生成/图生图/Qwen-edit-2511万物可修_2004538063986585602.json, 图片生成/图生图/Qwen-edit-2511万物移除_2005176520249405442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/44.tonnie-Qwen Edit 2059修手_2004540574411751426.json、图片生成/图生图/75.tonnie-2511万物精准移除_2011751771802181633.json、图片生成/图生图/Qwen-edit-2511-万物精准移除_2009156898662129666.json、图片生成/图生图/Qwen-edit-2511万物可修_2004538063986585602.json、图片生成/图生图/Qwen-edit-2511万物移除_2005176520249405442.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Blank`
- `ImageCompositeMasked`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 4/5 个有
- `GrowMaskWithBlur` —— 4/5 个有
- `InpaintCrop` —— 4/5 个有
- `InpaintStitch` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `Get Image Size` —— 3/5 个有
- `TextEncodeQwenImageEditPlus` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `GetImageSize+` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
