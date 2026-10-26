---
name: image_to_image_sampler_clip_unet_119
type: Image To Image
frequency: 4
level: moderate
coverage: 0.98225
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/clein 溶图工作流_2052269296637755394.json, 图片生成/图生图/flux-2-klein-单图编辑_2093259673406365697.json, 图片生成/图生图/flux2-9B-人物三视图生成_2054512404091949058.json, 图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/clein 溶图工作流_2052269296637755394.json、图片生成/图生图/flux-2-klein-单图编辑_2093259673406365697.json、图片生成/图生图/flux2-9B-人物三视图生成_2054512404091949058.json、图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `LayerMask: ImageToMask` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 20 | 4 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 20，4 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
