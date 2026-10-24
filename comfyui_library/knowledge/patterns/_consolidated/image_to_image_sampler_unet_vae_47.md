---
name: image_to_image_sampler_unet_vae_47
type: Image To Image
frequency: 4
level: strong
coverage: 0.91275
common_nodes: [CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, Get Image Size, Image Blank, Image Comparer (rgthree), ImageCompositeMasked, JoinImageWithAlpha, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein-无限扩图(颜色校正版)_2012322171997134849.json, 图片生成/图生图/Flux2-klein-无限扩图_2012182107996557314.json, 图片生成/图生图/Flux2-klein-物品移除（适用于小物品移除）_2012184119664447489.json, 图片生成/图生图/Qwen-edit-2511-无限扩图_2005084136446586881.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-无限扩图(颜色校正版)_2012322171997134849.json、图片生成/图生图/Flux2-klein-无限扩图_2012182107996557314.json、图片生成/图生图/Flux2-klein-物品移除（适用于小物品移除）_2012184119664447489.json、图片生成/图生图/Qwen-edit-2511-无限扩图_2005084136446586881.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `Get Image Size`
- `Image Blank`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CFGNorm` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `YC Color Match` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 6 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 6，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
