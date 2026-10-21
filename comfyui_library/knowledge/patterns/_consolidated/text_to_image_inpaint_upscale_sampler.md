---
name: text_to_image_inpaint_upscale_sampler
type: Text To Image
frequency: 5
level: weak
coverage: 0.8144
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image2512文生图+图生图+局部重绘_2007108957206220802.json, 图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json, 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json, 图片生成/文生图/【推荐】Qwen-Image2512文生图+图生图+局部重绘_2009842414927749121.json, 图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-Image2512文生图+图生图+局部重绘_2007108957206220802.json、图片生成/文生图/QwenEditRemix合集 文生图_图生图_局部重绘_图像编辑_2019803699635294209.json、图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json、图片生成/文生图/【推荐】Qwen-Image2512文生图+图生图+局部重绘_2009842414927749121.json、图片生成/文生图/局部重绘全能手｜QwenImageEditt图像编辑一站式_2096548610489016322.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `ControlNetInpaintingAliMamaApply` —— 4/5 个有
- `ControlNetLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Any Switch (rgthree)` —— 3/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `SDPoseDrawKeypoints` —— 2/5 个有
- `SDPoseKeypointExtractor` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `SetUnionControlNetType` —— 2/5 个有
- `Switch image [Crystools]` —— 2/5 个有
- `solarL_SaveImagesToZip` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 4 | 4 - 6 | 5 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 29% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 80 - 1664 | 5 | 22% |
| 高度 | 928 | 80 - 1920 | 5 | 13% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 6，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1664，5 个样本，取值分散，一致性仅 22%
- 高度 中位数 928，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 13%
- 高发问题（22/5 个样本）：Steps较低可能导致细节不足
