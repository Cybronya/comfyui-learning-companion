---
name: unknown_workflow_controlnet_lora_sampler_7
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.664143
common_nodes: [AIO_Preprocessor, CLIPLoader, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Fast Groups Bypasser (rgthree), ImageCompositeMasked, ImageScaleToTotalPixels, Int, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFastGrow, MaskToImage, PreviewImage, QwenEditConfigPreparer, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键万物迁移 精准涂抹版 +4服饰、饰品、换脸人_2040009605203369986.json, 图片生成/图生图/心然·寻源-服装替换和高清放大_2075129346150457346.json, 图片生成/图生图/最强一键换万物替换_2018685222472130562.json, 图片生成/图生图/服装替换和高清放大_2099051519277625345.json, 图片生成/图生图/服装替换和高清放大_2099422592154300418.json, 平台全量/一键万物迁移 精准涂抹版 +4K超清放大（0偏移+材质保留）服饰、饰品、换脸人_2022470088787496962.json, 平台全量/星绘-一键万物迁移（涂抹版）+4K超清放大（0偏移+材质保留）_2021868286023045121.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/一键万物迁移 精准涂抹版 +4服饰、饰品、换脸人_2040009605203369986.json、图片生成/图生图/心然·寻源-服装替换和高清放大_2075129346150457346.json、图片生成/图生图/最强一键换万物替换_2018685222472130562.json、图片生成/图生图/服装替换和高清放大_2099051519277625345.json、图片生成/图生图/服装替换和高清放大_2099422592154300418.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFastGrow`
- `MaskToImage`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `MaskFillHoles` —— 4/7 个有
- `CR Image Input Switch (4 way)` —— 3/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ImageScale` —— 3/7 个有
- `Mask Fill Holes` —— 3/7 个有
- `PlaySound|pysssss` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `RH_Nano_Banana2_Image2Image` —— 3/7 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/7 个有
- `RH_SeedreamV5ProImageToImage` —— 3/7 个有
- `SeedVR2BlockSwap` —— 3/7 个有
- `SeedVR2ExtraArgs` —— 3/7 个有
- `SeedVR2GGUF` —— 3/7 个有
- `TTP_Image_Assy` —— 3/7 个有
- `TTP_Image_Tile_Batch` —— 3/7 个有
- `TTP_Tile_image_size` —— 3/7 个有
- `easy imageBatchToImageList` —— 3/7 个有
- `easy imageListToImageBatch` —— 3/7 个有
- `easy imageSize` —— 3/7 个有
- `easy imageSizeBySide` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 2 | 2 - 2 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 2 - 2，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
