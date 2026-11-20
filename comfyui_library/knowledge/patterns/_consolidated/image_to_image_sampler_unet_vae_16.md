---
name: image_to_image_sampler_unet_vae_16
type: Image To Image
frequency: 12
level: weak
coverage: 0.933667
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实真人_2006954735986810882.json, 图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json, 图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json, 图片生成/图生图/千问Edit2511三图编辑_2004489688587141122.json, 图片生成/图生图/千问Edit2511单图编辑_2003703669726035969.json, 图片生成/图生图/千问Edit2511双图编辑_2004435367468167169.json, 图片生成/图生图/千问Qwen2511图像编辑换装｜全节点注释喂饭级教程_2063477606913241090.json, 图片生成/图生图/千问edit-老照片修复_2079961641495650306.json, 图片生成/图生图/千问edit视角转换_1987460531059625986.json, 图片生成/图生图/去水印_去文字qwen2511_2071627982585810945.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2077676821130338306.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2079437242732474369.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/动漫转写实真人_2006954735986810882.json、图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json、图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json、图片生成/图生图/千问Edit2511三图编辑_2004489688587141122.json、图片生成/图生图/千问Edit2511单图编辑_2003703669726035969.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CR Text` —— 11/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/12 个有
- `BackgroundEraseNetwork` —— 2/12 个有
- `ETN_LoadImageBase64` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `ImageConcanate` —— 2/12 个有
- `JC_ExtraOptions` —— 1/12 个有
- `JC_adv` —— 1/12 个有
- `PrimitiveString` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `Text Concatenate` —— 1/12 个有
- `TextEncodeQwenImageEdit` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 12 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 55% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 0.82 - 1 | 12 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.82 - 1，12 个样本，取值集中（一致性 95%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
