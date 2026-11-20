---
name: image_to_image_lora_sampler_vae_2
type: Image To Image
frequency: 20
level: strong
coverage: 0.89
common_nodes: [CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2046959707809652738.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2108091216880558082.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2011767661780275201.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097655330510561282.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097663834835218433.json, 图片生成/图生图/Qwen Image Edit 2511单图_多图编辑_2003658790107029506.json, 图片生成/图生图/Qwen image edit 2511 可视化灯光调节_2013071030331383810.json, 图片生成/图生图/Qwen+2511+图生图一致性_2005813572129226754.json, 图片生成/图生图/Qwen+Image+Edit+2511-单图多图编辑_2078322393449328641.json, 图片生成/图生图/Qwen+Image+Edit+2511-支持单图多图编辑 (1)_2016706323831857154.json, 图片生成/图生图/Qwen+Image-Edit-2511-AIO支持单图多图编辑_2077057145408937986.json, 图片生成/图生图/Qwen-Edit-2511 可视化重打光（lora强化版)_2012421686733312002.json, 图片生成/图生图/Qwen-image-edit-2511图像编辑（单图、双图、三图）_2025752704462626817.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095681119395082241.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095691718418067457.json, 图片生成/图生图/qwen2511角度控制_2003687770960871425.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2046959707809652738.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 19/20 个有
- `UNETLoader` —— 19/20 个有
- `VAELoader` —— 19/20 个有
- `EmptySD3LatentImage` —— 18/20 个有
- `Image Comparer (rgthree)` —— 17/20 个有
- `ImageScaleToTotalPixels` —— 17/20 个有
- `ImageConcanate` —— 15/20 个有
- `ImageConcatMulti` —— 15/20 个有
- `easy showAnything` —— 3/20 个有
- `ImageResizeKJv2` —— 2/20 个有
- `PreviewImage` —— 2/20 个有
- `QwenMultiangleLightningNode` —— 2/20 个有
- `CR Prompt List` —— 1/20 个有
- `CheckpointLoaderSimple` —— 1/20 个有
- `EmptyLatentImage` —— 1/20 个有
- `Int` —— 1/20 个有
- `PurgeVRAM_UTK` —— 1/20 个有
- `Text` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 20 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 95% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 95%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（24/20 个样本）：Steps较低可能导致细节不足
