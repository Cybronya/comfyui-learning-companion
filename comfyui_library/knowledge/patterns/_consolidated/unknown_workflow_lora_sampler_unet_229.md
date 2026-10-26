---
name: unknown_workflow_lora_sampler_unet_229
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.587
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, FluxKontextImageScale, FluxResolutionNode, GetNode, Image Comparer (rgthree), ImpactSwitch, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RH_LLMAPI_NODE, SaveImage, SetNode, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Edit2511单图编辑-可加遮罩_2005168324533252097.json, 图片生成/图生图/千问Edit2511单图编辑_2003659663717638145.json, 图片生成/图生图/千问Edit2511图像编辑-旧照片修复_2003709054725857281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_229

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问Edit2511单图编辑-可加遮罩_2005168324533252097.json、图片生成/图生图/千问Edit2511单图编辑_2003659663717638145.json、图片生成/图生图/千问Edit2511图像编辑-旧照片修复_2003709054725857281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Get Image Size` —— 2/3 个有
- `ImageComposite+` —— 2/3 个有
- `ImageCrop+` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `Is Mask Empty JK` —— 1/3 个有
- `MaxNode` —— 1/3 个有
- `QwenEditConfigPreparer` —— 1/3 个有
- `ResizeMask` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `workflow>面部修复` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
