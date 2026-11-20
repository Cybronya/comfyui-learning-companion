---
name: image_to_image_lora_sampler_clip_116
type: Image To Image
frequency: 4
level: weak
coverage: 0.78275
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DetailTransfer, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScale, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy imageSize, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/融图打光（还原细节）_1954399701959360514.json, 平台全量/【溶图打光换背景】修图产品重新打光电商产品提升质感 Kontext Lora 人像溶图打光 _ 人物_1988792897766035458.json, 平台全量/一键融图_1986307621416292354.json, 平台全量/光影融合溶图打光 电商合成 万物电商产品 产品场景合成阴影生成细节迁移海报合成_2050841556621508610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/融图打光（还原细节）_1954399701959360514.json、平台全量/【溶图打光换背景】修图产品重新打光电商产品提升质感 Kontext Lora 人像溶图打光 _ 人物_1988792897766035458.json、平台全量/一键融图_1986307621416292354.json、平台全量/光影融合溶图打光 电商合成 万物电商产品 产品场景合成阴影生成细节迁移海报合成_2050841556621508610.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
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
- `Seed (rgthree)` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `BiRefNetRMBG` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ImageBlend` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有
- `AILab_ImageCombiner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | 5 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.2 - 1 | 4 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，观测区间 5 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 33%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
