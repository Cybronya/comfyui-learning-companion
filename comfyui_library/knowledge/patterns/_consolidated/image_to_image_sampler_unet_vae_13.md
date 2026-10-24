---
name: image_to_image_sampler_unet_vae_13
type: Image To Image
frequency: 12
level: moderate
coverage: 0.87525
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实真人_2006954735986810882.json, 图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json, 图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json, 图片生成/图生图/千问Qwen2511图像编辑换装｜全节点注释喂饭级教程_2063477606913241090.json, 图片生成/图生图/千问edit-老照片修复_2079961641495650306.json, 图片生成/图生图/千问edit视角转换_1987460531059625986.json, 图片生成/图生图/去水印_去文字qwen2511_2071627982585810945.json, 图片生成/图生图/融图打光-透视纠正_2043942865646133249.json, 图片生成/图生图/课程演示-去水印_2075540632856260610.json, 图片生成/图生图/豆包图片去水印_高清修复_2082761030039588866.json, 图片生成/文生图/Qwen Edit 2511 图片去水印 全节点注释_2077810588885020674.json, 图片生成/文生图/Qwen Edit 2511单图编辑_2073294347310821377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/动漫转写实真人_2006954735986810882.json、图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json、图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json、图片生成/图生图/千问Qwen2511图像编辑换装｜全节点注释喂饭级教程_2063477606913241090.json、图片生成/图生图/千问edit-老照片修复_2079961641495650306.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

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
- `CR Text` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 6/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
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
| 采样步数 | 8 | 4 - 20 | 12 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 55% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 0.82 - 1 | 12 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，12 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.82 - 1，12 个样本，取值集中（一致性 95%）
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
