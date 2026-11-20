---
name: image_to_image_sampler_unet_vae_36
type: Image To Image
frequency: 5
level: strong
coverage: 0.8406
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 图像编辑_遮罩编辑_2004146251220328449.json, 图片生成/图生图/Qwen Edit 2511 零偏移编辑图像_2003862140756893698.json, 图片生成/图生图/Qwen-Edit+2511-细化改图-零偏移图生图_2036406339810889730.json, 图片生成/图生图/Qwen-Edit-2511 Anypose 精确控制人体姿势_2084960929535582210.json, 图片生成/图生图/应用级：千问单_双图编辑，和风整理_2008344909979328513.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 图像编辑_遮罩编辑_2004146251220328449.json、图片生成/图生图/Qwen Edit 2511 零偏移编辑图像_2003862140756893698.json、图片生成/图生图/Qwen-Edit+2511-细化改图-零偏移图生图_2036406339810889730.json、图片生成/图生图/Qwen-Edit-2511 Anypose 精确控制人体姿势_2084960929535582210.json、图片生成/图生图/应用级：千问单_双图编辑，和风整理_2008344909979328513.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/5 个有
- `Get Image Size` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `MaxNode` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `ReferenceLatent` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Int` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
