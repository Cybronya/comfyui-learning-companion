---
name: image_to_image_upscale_lora_sampler_22
type: Image To Image
frequency: 7
level: strong
coverage: 0.677286
common_nodes: [CLIPLoader, ConditioningZeroOut, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Q版手办动作迁移工作流_2058969579262668801.json, 图片生成/图生图/【Aaron寄语秋歌】一键转Q版工作流V1_2056685032944783362.json, 图片生成/图生图/一键转Q版工作流V1 (1)_2059448790507151362.json, 图片生成/图生图/一键转Q版工作流V1_2057519278815006722.json, 图片生成/图生图/一键转Q版工作流V1_2057651447432572929.json, 图片生成/图生图/一键转Q版工作流V1_2057700323195711490.json, 图片生成/图生图/一键转Q版工作流V1_2059158135604076546.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Q版手办动作迁移工作流_2058969579262668801.json、图片生成/图生图/【Aaron寄语秋歌】一键转Q版工作流V1_2056685032944783362.json、图片生成/图生图/一键转Q版工作流V1 (1)_2059448790507151362.json、图片生成/图生图/一键转Q版工作流V1_2057519278815006722.json、图片生成/图生图/一键转Q版工作流V1_2057651447432572929.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `孤海注释` —— 2/7 个有
- `BodyRatioMapperProportionTransfer` —— 1/7 个有
- `BodyRatioMapperSDPoseBoneScale` —— 1/7 个有
- `BodyRatioMapperSDPoseRender` —— 1/7 个有
- `BodyRatioMapperSDPoseTranslate` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `Easy_QwenEdit2509` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `SDPoseKeypointExtractor` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | sgm_uniform | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
