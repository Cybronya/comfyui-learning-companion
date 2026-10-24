---
name: image_to_image_upscale_lora_sampler_29
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8126
common_nodes: [CLIPLoader, CLIPTextEncode, CM_FloatToInt, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, PixaromaLoraLoader, PixaromaTextJoinTwo, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, YC Color Match]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 洗图 +放大（控尺寸）_2097156300693135361.json, 图片生成/图生图/Flux2_洗图_+放大控尺寸_2102922542515310593.json, 图片生成/图生图/Flux2_洗图_+放大控尺寸_2104384842224979969.json, 图片生成/图生图/Flux2_洗图_+放大控尺寸_2104753765705404418.json, 图片生成/图生图/flux2-局部重绘+放大_2101612616186687489.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2 洗图 +放大（控尺寸）_2097156300693135361.json、图片生成/图生图/Flux2_洗图_+放大控尺寸_2102922542515310593.json、图片生成/图生图/Flux2_洗图_+放大控尺寸_2104384842224979969.json、图片生成/图生图/Flux2_洗图_+放大控尺寸_2104753765705404418.json、图片生成/图生图/flux2-局部重绘+放大_2101612616186687489.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PixaromaLoraLoader`
- `PixaromaTextJoinTwo`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YC Color Match`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `Float` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `Kontext Inpainting Conditioning` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.04 | 0.04 - 1 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.04，观测区间 0.04 - 1，5 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.04，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
