---
name: image_to_image_sampler_clip_vae_29
type: Image To Image
frequency: 8
level: weak
coverage: 0.90475
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, ImageConcanate, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/USO原图加提示词 给主体换动作背景_1965042426693996546.json, 图片生成/图生图/kontext，花纹提取，提取万物_2038157564516503553.json, 图片生成/图生图/人物穿机甲上身_1998275786761232385.json, 图片生成/图生图/女生穿机甲_1998275467532754946.json, 图片生成/图生图/开源Flux Kontext Dev一句话图像编辑_1938408242026319874.json, 图片生成/图生图/机甲上身_1945025093413298177.json, 图片生成/图生图/机甲上身_2038794173079363586.json, 平台全量/Kontext-dev一句话换发色和背景_1938485528004354049.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/USO原图加提示词 给主体换动作背景_1965042426693996546.json、图片生成/图生图/kontext，花纹提取，提取万物_2038157564516503553.json、图片生成/图生图/人物穿机甲上身_1998275786761232385.json、图片生成/图生图/女生穿机甲_1998275467532754946.json、图片生成/图生图/开源Flux Kontext Dev一句话图像编辑_1938408242026319874.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
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
- `DualCLIPLoader` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `VAELoader` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ApplyFBCacheOnModel` —— 5/8 个有
- `DeepTranslatorTextNode` —— 5/8 个有
- `Primitive string multiline [Crystools]` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `Text` —— 2/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `FluxKontextImageScale` —— 1/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/8 个有
- `RH_Translator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 25 | 8 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 8 | 0% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
