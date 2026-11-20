---
name: text_to_image_lora_sampler_clip_371
type: Text To Image
frequency: 5
level: strong
coverage: 0.8976
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, ImageScaleToTotalPixels, JjkText, KSampler, LayerColor: ColorAdapter, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json, 图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json, 图片生成/图生图/一键换装万物迁移精准涂抹版｜图生图4K超清放大_2108437941113675777.json, 图片生成/图生图/摄影姿势迁移批量版｜角色一致性分镜出图高效套用_2114277678789517313.json, 图片生成/图生图/服装内衣换装升级版精准涂抹版加4K超清放大 电商服装展示_2108701892879671297.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_371

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json、图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json、图片生成/图生图/一键换装万物迁移精准涂抹版｜图生图4K超清放大_2108437941113675777.json、图片生成/图生图/摄影姿势迁移批量版｜角色一致性分镜出图高效套用_2114277678789517313.json、图片生成/图生图/服装内衣换装升级版精准涂抹版加4K超清放大 电商服装展示_2108701892879671297.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `easy promptReplace` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有
- `KOOK_SaveJPGImage` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `SDPoseOODLoader` —— 2/5 个有
- `SDPoseOODProcessor` —— 2/5 个有
- `SomethingToString` —— 2/5 个有
- `CompressImages` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `ImageListToBatch_` —— 1/5 个有
- `RHUploadZip_V2` —— 1/5 个有
- `SaveImageJPG_GH` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `workflow>123` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（20/5 个样本）：Steps较低可能导致细节不足
