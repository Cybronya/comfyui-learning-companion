---
name: image_to_image_sampler_clip_vae_29
type: Image To Image
frequency: 7
level: moderate
coverage: 0.898714
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, ImageConcanate, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/USO原图加提示词 给主体换动作背景_1965042426693996546.json, 图片生成/图生图/kontext，花纹提取，提取万物_2038157564516503553.json, 图片生成/图生图/人物穿机甲上身_1998275786761232385.json, 图片生成/图生图/女生穿机甲_1998275467532754946.json, 图片生成/图生图/开源Flux Kontext Dev一句话图像编辑_1938408242026319874.json, 图片生成/图生图/机甲上身_1945025093413298177.json, 图片生成/图生图/机甲上身_2038794173079363586.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/USO原图加提示词 给主体换动作背景_1965042426693996546.json、图片生成/图生图/kontext，花纹提取，提取万物_2038157564516503553.json、图片生成/图生图/人物穿机甲上身_1998275786761232385.json、图片生成/图生图/女生穿机甲_1998275467532754946.json、图片生成/图生图/开源Flux Kontext Dev一句话图像编辑_1938408242026319874.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `VAELoader` —— 6/7 个有
- `ApplyFBCacheOnModel` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `DeepTranslatorTextNode` —— 4/7 个有
- `Primitive string multiline [Crystools]` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `Text` —— 2/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `RH_Translator` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 7 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，7 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
