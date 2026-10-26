---
name: image_to_image_inpaint_sampler_clip_3
type: Image To Image
frequency: 6
level: strong
coverage: 0.8625
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, INPAINT_ExpandMask, Image Comparer (rgthree), ImageCompositeMasked, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewAny, RH_Translator, ReferenceLatent, SAM3_Detect, SaveImage, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-2-Kelin 零色差局部重绘 2 合 1 (手动蒙板+Sam3.1语义蒙板)_2113822604304932865.json, 图片生成/图生图/Flux-2-Kelin 零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2080550859699736578.json, 图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085015080047038466.json, 图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json, 图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json, 图片生成/图生图/局部重绘 语义识别 Sam3.1_2058768528865587202.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux-2-Kelin 零色差局部重绘 2 合 1 (手动蒙板+Sam3.1语义蒙板)_2113822604304932865.json、图片生成/图生图/Flux-2-Kelin 零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2080550859699736578.json、图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085015080047038466.json、图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json、图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `INPAINT_ExpandMask`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewAny`
- `RH_Translator`
- `ReferenceLatent`
- `SAM3_Detect`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 4/6 个有
- `ImpactSwitch` —— 4/6 个有
- `MaskFillHoles` —— 4/6 个有
- `ImageAndMaskPreview` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
