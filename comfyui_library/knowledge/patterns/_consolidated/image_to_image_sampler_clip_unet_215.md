---
name: image_to_image_sampler_clip_unet_215
type: Image To Image
frequency: 2
level: weak
coverage: 0.8075
common_nodes: [CLIPTextEncode, ColorMatch, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageScaleBy, KSampler, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, PreviewImage, PrimitiveFloat, ReferenceLatent, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/人物一致性Kontext版ControlNet_1962059356340731905.json, 平台全量/kontext灰度图深度图+高清放大+抠图_1979376799815733250.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_215

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物一致性Kontext版ControlNet_1962059356340731905.json、平台全量/kontext灰度图深度图+高清放大+抠图_1979376799815733250.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1.5 | - | 1 | 100% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
