---
name: image_to_image_lora_sampler_clip_41
type: Image To Image
frequency: 7
level: weak
coverage: 0.754429
common_nodes: [BiRefNetRMBG, CLIPTextEncode, ConditioningZeroOut, DetailTransfer, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), ImageScale, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RMBG, ReferenceLatent, SaveImage, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy imageSize, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️------Qwen溶图+Flux打光+Krea修复-溶图合成全流程_2009445979153502210.json, 图片生成/图生图/产品溶图打光柔光工作流-电商合成_2064724074877771777.json, 图片生成/图生图/溶图+打光v2_2029889320974290946.json, 图片生成/图生图/溶图打光工作流-电商合成全流程_1955254846226141185.json, 图片生成/图生图/溶图打光工作流-电商合成全流程_2049087824917438466.json, 图片生成/图生图/融图工作流_1960321016218251265.json, 图片生成/图生图/融图打光-kontext.(自定义构图）_1954178993832521729.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️------Qwen溶图+Flux打光+Krea修复-溶图合成全流程_2009445979153502210.json、图片生成/图生图/产品溶图打光柔光工作流-电商合成_2064724074877771777.json、图片生成/图生图/溶图+打光v2_2029889320974290946.json、图片生成/图生图/溶图打光工作流-电商合成全流程_1955254846226141185.json、图片生成/图生图/溶图打光工作流-电商合成全流程_2049087824917438466.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `BiRefNetRMBG`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 6/7 个有
- `Seed (rgthree)` —— 6/7 个有
- `ConstrainImage|pysssss` —— 5/7 个有
- `JjkText` —— 5/7 个有
- `LayerUtility: ImageBlend` —— 5/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/7 个有
- `AutoImageResize` —— 1/7 个有
- `CFGNorm` —— 1/7 个有
- `CLIPLoader` —— 1/7 个有
- `Cut By Mask` —— 1/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `Get resolution [Crystools]` —— 1/7 个有
- `InvertMask (segment anything)` —— 1/7 个有
- `LayerColor: ColorAdapter` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `easy imageScaleDown` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 20 | 7 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 7 | 27% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 20，7 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，7 个样本，取值分散，一致性仅 27%
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
