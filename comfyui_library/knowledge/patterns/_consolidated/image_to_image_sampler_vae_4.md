---
name: image_to_image_sampler_vae_4
type: Image To Image
frequency: 24
level: moderate
coverage: 0.910167
common_nodes: [CFGNorm, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511-万物一键三视图_2005152885329588225.json, 图片生成/图生图/Qwen Image Edit 2511-三视图_2004960784432201729.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2046959707809652738.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2108091216880558082.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2011767661780275201.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097655330510561282.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097663834835218433.json, 图片生成/图生图/Qwen Image Edit 2511单图_多图编辑_2003658790107029506.json, 图片生成/图生图/Qwen+2511+图生图一致性_2005813572129226754.json, 图片生成/图生图/Qwen+Image+Edit+2511-单图多图编辑_2078322393449328641.json, 图片生成/图生图/Qwen+Image+Edit+2511-支持单图多图编辑 (1)_2016706323831857154.json, 图片生成/图生图/Qwen+Image-Edit-2511-AIO支持单图多图编辑_2077057145408937986.json, 图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095681119395082241.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095691718418067457.json, 图片生成/图生图/Qwen千问Image Edit 2511 多图编辑工作流_1953374181926817794.json, 图片生成/图生图/【AI小王子】86.Qwen+2511+图生图一致性之王！_2048651007839707137.json, 图片生成/图生图/人物换装+换背景V2_2004104139988738050.json, 图片生成/图生图/千问Qwen+Image+Edit+2511-三图多图编辑（加速版）_2005619327858606082.json, 图片生成/文生图/Qwen Edit 2511双图编辑_2073294666874843138.json, 图片生成/文生图/测试v2_2028368389479075842.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511-万物一键三视图_2005152885329588225.json、图片生成/图生图/Qwen Image Edit 2511-三视图_2004960784432201729.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 23/24 个有
- `FluxKontextMultiReferenceLatentMethod` —— 23/24 个有
- `LoraLoaderModelOnly` —— 23/24 个有
- `UNETLoader` —— 23/24 个有
- `VAELoader` —— 23/24 个有
- `ImageConcatMulti` —— 21/24 个有
- `Image Comparer (rgthree)` —— 20/24 个有
- `ImageConcanate` —— 20/24 个有
- `EmptySD3LatentImage` —— 18/24 个有
- `CR Text` —— 2/24 个有
- `EmptyLatentImage` —— 2/24 个有
- `ImageBatch` —— 2/24 个有
- `ImageConcatFromBatch` —— 2/24 个有
- `ImageListToBatch+` —— 2/24 个有
- `KepStringList` —— 2/24 个有
- `CheckpointLoaderSimple` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 24 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 24 | 72% |
| 采样算法 | euler | - | 24 | 96% |
| 调度器 | simple | - | 24 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，24 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，24 个样本
- 采样算法 最常用 euler，24 个样本，一致性 96%
- 调度器 最常用 simple，24 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（30/24 个样本）：Steps较低可能导致细节不足
