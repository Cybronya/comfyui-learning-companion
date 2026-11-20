---
name: unknown_workflow_lora_sampler_unet_224
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.614
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, FluxKontextImageScale, FluxResolutionNode, GetNode, Image Comparer (rgthree), ImpactSwitch, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RH_LLMAPI_NODE, SaveImage, SetNode, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Edit2511单图编辑-可加遮罩_2005168324533252097.json, 图片生成/图生图/千问Edit2511单图编辑_2003659663717638145.json, 图片生成/图生图/千问Edit2511图像编辑-旧照片修复_2003709054725857281.json, 平台全量/Qwen-Edit2511老照片修复+高清放大_2027796478789423106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_224

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千问Edit2511单图编辑-可加遮罩_2005168324533252097.json、图片生成/图生图/千问Edit2511单图编辑_2003659663717638145.json、图片生成/图生图/千问Edit2511图像编辑-旧照片修复_2003709054725857281.json、平台全量/Qwen-Edit2511老照片修复+高清放大_2027796478789423106.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `FluxResolutionNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `Get Image Size` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageComposite+` —— 2/4 个有
- `ImageCrop+` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `Is Mask Empty JK` —— 2/4 个有
- `MaxNode` —— 2/4 个有
- `QwenEditConfigPreparer` —— 2/4 个有
- `ResizeMask` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `INTConstant` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `TTP_Image_Assy` —— 1/4 个有
- `TTP_Image_Tile_Batch` —— 1/4 个有
- `TTP_Tile_image_size` —— 1/4 个有
- `TextInputBasic` —— 1/4 个有
- `easy imageBatchToImageList` —— 1/4 个有
- `easy imageListToImageBatch` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy imageSizeBySide` —— 1/4 个有
- `workflow>面部修复` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
