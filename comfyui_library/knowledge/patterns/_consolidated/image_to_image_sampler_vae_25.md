---
name: image_to_image_sampler_vae_25
type: Image To Image
frequency: 5
level: strong
coverage: 0.8836
common_nodes: [CLIPLoader, ImageConcanate, ImageFromBatch, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/杀马特造型抖音超火人物一致性加速版_1982011855520579586.json, 图片生成/图生图/真人+动漫-一图转15图_1982670915924303873.json, 图片生成/图生图/真人一图生成15视角_1981880065791279105.json, 图片生成/图生图/🍲一图生成15视角【真人 动漫均可】🍲_1981639749955928065.json, 图片生成/图生图/👾怪獸-多视角一致性【真人 动漫】👾_1981982012569460737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/杀马特造型抖音超火人物一致性加速版_1982011855520579586.json、图片生成/图生图/真人+动漫-一图转15图_1982670915924303873.json、图片生成/图生图/真人一图生成15视角_1981880065791279105.json、图片生成/图生图/🍲一图生成15视角【真人 动漫均可】🍲_1981639749955928065.json、图片生成/图生图/👾怪獸-多视角一致性【真人 动漫】👾_1981982012569460737.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `TextEncodeQwenImageEdit` —— 4/5 个有
- `Fast Bypasser (rgthree)` —— 3/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/5 个有
- `NunchakuQwenImageDiTLoader` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `Text Load Line From File` —— 2/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ReplaceText` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `UNETLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
