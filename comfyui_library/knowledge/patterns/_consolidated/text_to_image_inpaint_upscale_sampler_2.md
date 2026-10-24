---
name: text_to_image_inpaint_upscale_sampler_2
type: Text To Image
frequency: 3
level: weak
coverage: 0.787333
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskPreview+, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json, 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json, 图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json、图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json、图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `ControlNetInpaintingAliMamaApply` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `ImagePadForOutpaint` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SDPoseDrawKeypoints` —— 2/3 个有
- `SDPoseKeypointExtractor` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `Switch image [Crystools]` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1080 | 3 | 0% |
| 高度 | 80 | 80 - 1920 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，3 个样本，取值分散，一致性仅 0%
- 高发问题（16/3 个样本）：Steps较低可能导致细节不足
