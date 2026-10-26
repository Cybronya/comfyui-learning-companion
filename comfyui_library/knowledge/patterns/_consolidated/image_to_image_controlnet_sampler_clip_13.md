---
name: image_to_image_controlnet_sampler_clip_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.614667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, Fast Groups Bypasser (rgthree), GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, KSampler, LanPaint_MaskBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AA--Zimage-局部重绘+4K放大_2006950200786554882.json, 图片生成/图生图/局部重绘_2059477250227138562.json, 图片生成/图生图/局部重绘_2059506283165868033.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AA--Zimage-局部重绘+4K放大_2006950200786554882.json、图片生成/图生图/局部重绘_2059477250227138562.json、图片生成/图生图/局部重绘_2059506283165868033.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Fast Groups Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `KSampler`
- `LanPaint_MaskBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ImageToMask` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `INTConstant` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
