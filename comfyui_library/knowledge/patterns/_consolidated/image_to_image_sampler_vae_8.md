---
name: image_to_image_sampler_vae_8
type: Image To Image
frequency: 14
level: moderate
coverage: 0.973571
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json, 图片生成/图生图/qwen-Edit（智能修图）0.1_2042504294313758722.json, 图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json, 图片生成/图生图/qwen-edit-2511精准控制+零偏移_2003639178539769858.json, 图片生成/图生图/qwen-edit2511图转马克笔厚涂_2056669779385217025.json, 图片生成/图生图/qwen-edit2511融图_2004036915668107266.json, 图片生成/图生图/qwen-image-edit2511-去水印-标准版-（必收藏）_2057010466009997314.json, 图片生成/图生图/qwen2511图片编辑，改变照片风格、色调、添加元素、修改元素、多镜头照片，多图融合，_2007099096045199361.json, 图片生成/图生图/qwen2511图转3d_2037359877261103105.json, 图片生成/图生图/▶千问Edit2511GGUF流 1-3图编辑 效果更高版_2048971550191263745.json, 图片生成/图生图/图片转色块 Qwen Image Edit 2511_2052014658105692161.json, 图片生成/图生图/爆火新年祭_2005453436986552322.json, 图片生成/图生图/🦄Qwen-edit-2511精准控制🎯天下无腰_2022653232950026242.json, 图片生成/文生图/B妮B妳_Qwen Edit-2511_N_S_F_W_汇总_2019388996597583874.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json、图片生成/图生图/qwen-Edit（智能修图）0.1_2042504294313758722.json、图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json、图片生成/图生图/qwen-edit-2511精准控制+零偏移_2003639178539769858.json、图片生成/图生图/qwen-edit2511图转马克笔厚涂_2056669779385217025.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `CFGNorm` —— 9/14 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/14 个有
- `ImageScaleToTotalPixels` —— 7/14 个有
- `ReferenceLatent` —— 6/14 个有
- `EmptySD3LatentImage` —— 5/14 个有
- `DifferentialDiffusion` —— 2/14 个有
- `InpaintModelConditioning` —— 2/14 个有
- `MaskFillHoles` —— 2/14 个有
- `UnetLoaderGGUF` —— 2/14 个有
- `CLIPTextEncode` —— 1/14 个有
- `CheckpointLoaderSimple` —— 1/14 个有
- `ConditioningZeroOut` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `GoogleTranslator` —— 1/14 个有
- `HAIGC_SaveImagesToZip` —— 1/14 个有
- `Image Comparer (rgthree)` —— 1/14 个有
- `easy promptList` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 9 | 14 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 14 | 66% |
| 采样算法 | euler | - | 14 | 50% |
| 调度器 | simple | - | 14 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 9，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 50%
- 调度器 最常用 simple，14 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（18/14 个样本）：Steps较低可能导致细节不足
