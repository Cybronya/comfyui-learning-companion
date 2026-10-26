---
name: unknown_workflow_inpaint_sampler_clip_31
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85625
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Redux 换服装_1896208365628555266.json, 图片生成/图生图/一键快速换装_1900359679300595714.json, 图片生成/图生图/石头自动抠图_1955122078221570050.json, 图片生成/文生图/面料生成衣服_1896823389481279490.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Redux 换服装_1896208365628555266.json、图片生成/图生图/一键快速换装_1900359679300595714.json、图片生成/图生图/石头自动抠图_1955122078221570050.json、图片生成/文生图/面料生成衣服_1896823389481279490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `EmptyImage` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `InvertMask` —— 3/4 个有
- `LayerMask: MaskPreview` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `easy imageSplitGrid` —— 3/4 个有
- `easy imagesSplitImage` —— 3/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text Concatenate (JPS)` —— 2/4 个有
- `Text Prompt (JPS)` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `Image To Mask` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `JanusImageUnderstanding` —— 1/4 个有
- `JanusModelLoader` —— 1/4 个有
- `Joy_caption` —— 1/4 个有
- `Joy_caption_load` —— 1/4 个有
- `LayerMask: LoadFlorence2Model` —— 1/4 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ReduxAdvanced` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 30 | 4 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
