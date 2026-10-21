---
name: unknown_workflow_lora_sampler_unet_38
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.67
common_nodes: [CFGNorm, CLIPLoader, CropWithPadInfo, Image Comparer (rgthree), Image Rembg (Remove Background), ImageResizeKJv2, ImageScaleBy, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask To Image (mtb), MaskPreview, MaskToImage, ModelSamplingAuraFlow, PreviewAny, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditAny2Image, QwenEditConfigPreparer, QwenEditListExtractor, QwenEditOutputExtractor, SaveImage, TTP_Expand_And_Mask, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2511无痕换头重绘贴回大师版_2027381547103424514.json, 图片生成/文生图/重绘贴回-2511局部重绘-万物迁移_2017885601479004162.json, 图片生成/文生图/重绘贴回-2511局部重绘_2018213964676603905.json, 视频生成/文生视频/Qwen 2511 局部角色替换工作流_2041678315030843394.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/2511无痕换头重绘贴回大师版_2027381547103424514.json、图片生成/文生图/重绘贴回-2511局部重绘-万物迁移_2017885601479004162.json、图片生成/文生图/重绘贴回-2511局部重绘_2018213964676603905.json、视频生成/文生视频/Qwen 2511 局部角色替换工作流_2041678315030843394.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `Image Rembg (Remove Background)`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask To Image (mtb)`
- `MaskPreview`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAny2Image`
- `QwenEditConfigPreparer`
- `QwenEditListExtractor`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TTP_Expand_And_Mask`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `JWImageExtractFromBatch` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 4 | 2% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，4 个样本，取值分散，一致性仅 2%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
