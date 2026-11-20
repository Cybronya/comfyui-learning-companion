---
name: unknown_workflow_controlnet_inpaint_upscale_3
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.79325
common_nodes: [Anything Everywhere3, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImagePadForOutpaint, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskPreview+, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2511合集（角色修改）good_2046840929314672642.json, 图片生成/图生图/QwenEdit2511合集（角色设计）_2041860060250378242.json, 图片生成/图生图/【最推荐】QwenEdit2511-AIOV18图片超强合集（你懂的，支持本地解码）_2009839988774543362.json, 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能_2094527878292664322.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenEdit2511合集（角色修改）good_2046840929314672642.json、图片生成/图生图/QwenEdit2511合集（角色设计）_2041860060250378242.json、图片生成/图生图/【最推荐】QwenEdit2511-AIOV18图片超强合集（你懂的，支持本地解码）_2009839988774543362.json、图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能_2094527878292664322.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `INPAINT_MaskedFill` —— 3/4 个有
- `SDPoseOODLoader` —— 3/4 个有
- `SDPoseOODProcessor` —— 3/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `SDPoseDrawKeypoints` —— 1/4 个有
- `SDPoseKeypointExtractor` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Switch image [Crystools]` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有
- `UNETLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（20/4 个样本）：Steps较低可能导致细节不足
