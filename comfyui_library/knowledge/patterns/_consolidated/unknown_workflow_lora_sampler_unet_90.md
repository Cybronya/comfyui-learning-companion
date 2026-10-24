---
name: unknown_workflow_lora_sampler_unet_90
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.685286
common_nodes: [CFGNorm, CLIPLoader, CropWithPadInfo, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleBy, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskPreview, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 局部角色替换工作流_2042594620185513986.json, 图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json, 图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json, 图片生成/文生图/2511无痕换头重绘贴回大师版_2027381547103424514.json, 图片生成/文生图/重绘贴回-2511局部重绘-万物迁移_2017885601479004162.json, 图片生成/文生图/重绘贴回-2511局部重绘_2018213964676603905.json, 视频生成/文生视频/Qwen 2511 局部角色替换工作流_2041678315030843394.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 局部角色替换工作流_2042594620185513986.json、图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json、图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json、图片生成/文生图/2511无痕换头重绘贴回大师版_2027381547103424514.json、图片生成/文生图/重绘贴回-2511局部重绘-万物迁移_2017885601479004162.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LayerUtility: ImageReel` —— 6/7 个有
- `LayerUtility: ImageReelComposit` —— 6/7 个有
- `MaskToImage` —— 6/7 个有
- `QwenEditAny2Image` —— 6/7 个有
- `QwenEditListExtractor` —— 6/7 个有
- `TTP_Expand_And_Mask` —— 6/7 个有
- `Image Rembg (Remove Background)` —— 5/7 个有
- `Mask To Image (mtb)` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `CLIPTextEncode` —— 3/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `SAM3_Detect` —— 2/7 个有
- `JWImageExtractFromBatch` —— 1/7 个有
- `RMBG` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | sgm_uniform | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
