---
name: image_to_image_lora_sampler_clip_106
type: Image To Image
frequency: 4
level: moderate
coverage: 0.823
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DF_Integer, DualCLIPLoader, FluxGuidance, ImageListToBatch+, ImpactImageBatchToImageList, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: Seed, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_image_edit迄今超强6步快速出万物提取衣物+可选4K高清放大_1964971680823169026.json, 平台全量/Kontext-DEV迄今超强8步万物模糊_低分辨率图像高分辨率修复来袭+高清4K放大✨_1976200777020653570.json, 平台全量/Qwen-Image-Edit迄今超强万物产品溶图打光神器_1975411336698048513.json, 平台全量/kontext-dev迄今超强8步纠正场景背景透视角度匹配物体溶图重打光+可选4K高清出图_1962732827903176706.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen_image_edit迄今超强6步快速出万物提取衣物+可选4K高清放大_1964971680823169026.json、平台全量/Kontext-DEV迄今超强8步万物模糊_低分辨率图像高分辨率修复来袭+高清4K放大✨_1976200777020653570.json、平台全量/Qwen-Image-Edit迄今超强万物产品溶图打光神器_1975411336698048513.json、平台全量/kontext-dev迄今超强8步纠正场景背景透视角度匹配物体溶图重打光+可选4K高清出图_1962732827903176706.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Integer`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToBatch+`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: Seed`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `CFGNorm` —— 2/4 个有
- `CLIPLoader` —— 2/4 个有
- `ImageColorMatch+` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `KSampler (Efficient)` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `FloatConstant` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `TTP_text_mix` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 4 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，4 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
