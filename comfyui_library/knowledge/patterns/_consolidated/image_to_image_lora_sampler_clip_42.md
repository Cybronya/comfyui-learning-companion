---
name: image_to_image_lora_sampler_clip_42
type: Image To Image
frequency: 8
level: strong
coverage: 0.913375
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), ImageConcanate, ImageConcatMulti, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveBoolean, ReferenceLatent, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json", 图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json, 图片生成/图生图/一键换装-FireRed-image-edit-1.1_2108017290770997249.json, 图片生成/图生图/一键换装-升级版一键万物迁移_精准涂抹版_+4K超清放大_2112438647998996482.json, 图片生成/图生图/一键换装-升级版一键万物迁移_精准涂抹版_+4K超清放大_2114998757359185922.json, 图片生成/图生图/服装内衣换装-升级版 精准涂抹版 +4K超清放大_2108106404539224066.json, 平台全量/一键换装-FireRed-image-edit-1.1_2041112266677948417.json, 平台全量/任意服装姿势一键迁移--Qwen Rapid AIO V23_2040030744965287937.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json、图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json、图片生成/图生图/一键换装-FireRed-image-edit-1.1_2108017290770997249.json、图片生成/图生图/一键换装-升级版一键万物迁移_精准涂抹版_+4K超清放大_2112438647998996482.json、图片生成/图生图/一键换装-升级版一键万物迁移_精准涂抹版_+4K超清放大_2114998757359185922.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `easy imageColorMatch` —— 7/8 个有
- `easy promptReplace` —— 7/8 个有
- `KOOK_SaveJPGImage` —— 5/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/8 个有
- `SDPoseOODLoader` —— 1/8 个有
- `SDPoseOODProcessor` —— 1/8 个有
- `SaveImageAndMetadata_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | sgm_uniform | - | 8 | 88% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 88%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，8 个样本，取值集中（一致性 100%）
- 高发问题（24/8 个样本）：Steps较低可能导致细节不足
