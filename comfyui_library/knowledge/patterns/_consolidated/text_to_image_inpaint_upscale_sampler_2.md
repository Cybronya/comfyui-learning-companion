---
name: text_to_image_inpaint_upscale_sampler_2
type: Text To Image
frequency: 4
level: weak
coverage: 0.793
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, MaskPreview+, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json, 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json, 图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json, 平台全量/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2095742649096560641.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json、图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json、图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json、平台全量/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2095742649096560641.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Text` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `ControlNetInpaintingAliMamaApply` —— 2/4 个有
- `ControlNetLoader` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `SDPoseDrawKeypoints` —— 2/4 个有
- `SDPoseKeypointExtractor` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `Switch image [Crystools]` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `孤海注释` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 580 | 80 - 1080 | 4 | 14% |
| 高度 | 1000 | 80 - 1920 | 4 | 8% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 580，观测区间 80 - 1080，4 个样本，取值分散，一致性仅 14%
- 高度 中位数 1000，观测区间 80 - 1920，4 个样本，取值分散，一致性仅 8%
- 高发问题（20/4 个样本）：Steps较低可能导致细节不足
