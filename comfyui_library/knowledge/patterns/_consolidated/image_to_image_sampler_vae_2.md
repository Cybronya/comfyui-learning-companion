---
name: image_to_image_sampler_vae_2
type: Image To Image
frequency: 31
level: strong
coverage: 0.895032
common_nodes: [CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2046959707809652738.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2108091216880558082.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2011767661780275201.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097655330510561282.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑改图修图迁移换装修复千问2511图像编辑_2097663834835218433.json, 图片生成/图生图/Qwen Image Edit 2511单图_多图编辑_2003658790107029506.json, 图片生成/图生图/Qwen image edit 2511 可视化灯光调节_2013071030331383810.json, 图片生成/图生图/Qwen+2511+图生图一致性_2005813572129226754.json, 图片生成/图生图/Qwen+Image+Edit+2511-单图多图编辑_2078322393449328641.json, 图片生成/图生图/Qwen+Image+Edit+2511-支持单图多图编辑 (1)_2016706323831857154.json, 图片生成/图生图/Qwen+Image-Edit-2511-AIO支持单图多图编辑_2077057145408937986.json, 图片生成/图生图/Qwen-Edit-2511 可视化重打光（lora强化版)_2012421686733312002.json, 图片生成/图生图/Qwen-image-edit-2511图像编辑（单图、双图、三图）_2025752704462626817.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095681119395082241.json, 图片生成/图生图/Qwen_Image_Edit_2511-支持单图多图编辑_2095691718418067457.json, 图片生成/图生图/Qwen千问Image Edit 2511 多图编辑工作流_1953374181926817794.json, 图片生成/图生图/【AI小王子】86.Qwen+2511+图生图一致性之王！_2048651007839707137.json, 图片生成/图生图/一键氛围打光_2011310291442733057.json, 图片生成/图生图/人物换装+换背景V2_2004104139988738050.json, 图片生成/图生图/千问Qwen+Image+Edit+2511-三图多图编辑（加速版）_2005619327858606082.json, 图片生成/图生图/可视化灯光调节(重打光lora强化版)_2021046893047980033.json, 图片生成/图生图/图像人物重新打光电商商品打精修千问模型plus_2077283170759827458.json, 图片生成/图生图/图像重打光 Qwen2511_2036012882982346753.json, 图片生成/图生图/图像重打光 Qwen2511_2076938070133395457.json, 图片生成/图生图/图像重打光_Qwen2511_2083573156970852354.json, 图片生成/图生图/图像重打光_Qwen2511_2095782087520514050.json, 图片生成/图生图/图像重打光_Qwen2511_2096073652218449921.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004755728197971970.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2026560006014898177.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2038424007581634562.json、图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2046959707809652738.json…）

- **类型**：Image To Image
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 31 个 workflow 都包含：
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 30/31 个有
- `LoraLoaderModelOnly` —— 30/31 个有
- `UNETLoader` —— 30/31 个有
- `VAELoader` —— 30/31 个有
- `EmptySD3LatentImage` —— 28/31 个有
- `ImageScaleToTotalPixels` —— 28/31 个有
- `ImageConcanate` —— 19/31 个有
- `ImageConcatMulti` —— 19/31 个有
- `Image Comparer (rgthree)` —— 18/31 个有
- `QwenMultiangleLightningNode` —— 10/31 个有
- `easy showAnything` —— 10/31 个有
- `EmptyLatentImage` —— 2/31 个有
- `ImageResizeKJv2` —— 2/31 个有
- `CR Text` —— 1/31 个有
- `CheckpointLoaderSimple` —— 1/31 个有
- `PreviewImage` —— 1/31 个有
- `Text` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 31 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 31 | 100% |
| 采样算法 | euler | - | 31 | 97% |
| 调度器 | simple | - | 31 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，31 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，31 个样本，一致性 97%
- 调度器 最常用 simple，31 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（35/31 个样本）：Steps较低可能导致细节不足
