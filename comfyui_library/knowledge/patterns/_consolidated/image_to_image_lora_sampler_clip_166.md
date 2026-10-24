---
name: image_to_image_lora_sampler_clip_166
type: Image To Image
frequency: 2
level: weak
coverage: 0.915
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DetailerForEach, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/白底产品添加草地场景_2004385746456899585.json, 图片生成/图生图/草地草坪_2094646127432921090.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/白底产品添加草地场景_2004385746456899585.json、图片生成/图生图/草地草坪_2094646127432921090.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Anything Everywhere3` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/2 个有
- `LayerUtility: ImageBlend` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
