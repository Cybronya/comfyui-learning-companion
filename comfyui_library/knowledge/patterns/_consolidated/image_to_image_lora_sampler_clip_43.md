---
name: image_to_image_lora_sampler_clip_43
type: Image To Image
frequency: 6
level: strong
coverage: 0.934833
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImpactInt, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2 Klein产品溶图6.0万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2097978983215353857.json, 图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2091717490102591490.json, 图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json, 图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092608823822475265.json, 图片生成/图生图/F.2_Klein产品溶图6.0万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2098204967990554625.json, 图片生成/图生图/FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/F.2 Klein产品溶图6.0万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2097978983215353857.json、图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2091717490102591490.json、图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json、图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092608823822475265.json、图片生成/图生图/F.2_Klein产品溶图6.0万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2098204967990554625.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `FastCanvas` —— 5/6 个有
- `FastCanvasTool` —— 5/6 个有
- `ImageCropper` —— 5/6 个有
- `easy imageRemBg` —— 5/6 个有
- `GLM_Translation_Text` —— 2/6 个有
- `MultiTextConcatenate` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `ImageScaleBy` —— 1/6 个有
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
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
