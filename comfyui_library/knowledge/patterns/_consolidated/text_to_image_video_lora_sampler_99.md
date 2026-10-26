---
name: text_to_image_video_lora_sampler_99
type: Text To Image
frequency: 9
level: strong
coverage: 0.751778
common_nodes: [ACE_TextConcatenate, CLIPLoader, CLIPTextEncode, CR Split String, ConditioningZeroOut, DiffusionModelLoaderKJ, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, GODMT_CreateList, GetImageSize, GetNode, ImageBatchExtendWithOverlap, ImageConcatenate_UTK, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MultiLinePromptIndex, PreviewImage, ProcessString, RH_Captioner, SetNode, Text, TextConcatenate, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy imageListToImageBatch, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.2漫剧全自动图生视频_2013141859459145729.json, 视频生成/图生视频/漫剧全自动 图生视频 AI短剧_2019041048890183682.json, 视频生成/图生视频/漫剧全自动图生视频_2066791164149325825.json, 视频生成/图生视频/漫剧全自动图生视频_2067059488955396098.json, 视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2014235252520128514.json, 视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2015805251634339842.json, 视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2046425306088611841.json, 视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2051860948775911426.json, 视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2054119413804216321.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_99

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/wan2.2漫剧全自动图生视频_2013141859459145729.json、视频生成/图生视频/漫剧全自动 图生视频 AI短剧_2019041048890183682.json、视频生成/图生视频/漫剧全自动图生视频_2066791164149325825.json、视频生成/图生视频/漫剧全自动图生视频_2067059488955396098.json、视频生成/图生视频/漫剧全自动图生视频_一气呵成版_2014235252520128514.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `ACE_TextConcatenate`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Split String`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `GODMT_CreateList`
- `GetImageSize`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageConcatenate_UTK`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiLinePromptIndex`
- `PreviewImage`
- `ProcessString`
- `RH_Captioner`
- `SetNode`
- `Text`
- `TextConcatenate`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy imageListToImageBatch`
- `easy indexAnything`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
