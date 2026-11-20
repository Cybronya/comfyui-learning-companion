---
name: image_to_image_lora_sampler_clip_149
type: Image To Image
frequency: 3
level: strong
coverage: 0.872
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DetailerForEach, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/白底产品添加草地场景_2004385746456899585.json, 图片生成/图生图/草地草坪_2094646127432921090.json, 平台全量/草地草坪 _ 修复_1875929767714185218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/白底产品添加草地场景_2004385746456899585.json、图片生成/图生图/草地草坪_2094646127432921090.json、平台全量/草地草坪 _ 修复_1875929767714185218.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailerForEach`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ConstrainImage|pysssss` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Image Overlay` —— 2/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LayerUtility: RestoreCropBox` —— 1/3 个有
- `preview_mask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
