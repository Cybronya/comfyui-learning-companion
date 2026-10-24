---
name: image_to_image_upscale_sampler_clip_27
type: Image To Image
frequency: 4
level: moderate
coverage: 0.95975
common_nodes: [CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image最新千问图生图高清放大版直出2K_1999060294070566914.json, 图片生成/图生图/flux2-双图融合-标准版-（必收藏）_2052713860611747841.json, 图片生成/图生图/flux2-图像去油腻增强细节高清放大-标准版-（必收藏）_2053825217205678081.json, 图片生成/图生图/kontext蒙版消除_2087355554166562817.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-Image最新千问图生图高清放大版直出2K_1999060294070566914.json、图片生成/图生图/flux2-双图融合-标准版-（必收藏）_2052713860611747841.json、图片生成/图生图/flux2-图像去油腻增强细节高清放大-标准版-（必收藏）_2053825217205678081.json、图片生成/图生图/kontext蒙版消除_2087355554166562817.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `easy getNode` —— 2/4 个有
- `easy setNode` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `Image Compare (mtb)` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Qwen3VL_Advanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 20 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 20，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
