---
name: image_to_image_sampler_clip_unet_129
type: Image To Image
frequency: 3
level: strong
coverage: 0.934333
common_nodes: [AutoImageResize, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Cut By Mask, FluxGuidance, Get resolution [Crystools], Image Comparer (rgthree), KSampler, LoadImage, MaskToImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012436110101716994.json, 图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json, 图片生成/图生图/FLUX.2 Klein 局部重绘＋移除物体_2012497850864766977.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012436110101716994.json、图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json、图片生成/图生图/FLUX.2 Klein 局部重绘＋移除物体_2012497850864766977.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `AutoImageResize`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Cut By Mask`
- `FluxGuidance`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `InvertMask (segment anything)` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `MaskFillHoles` —— 1/3 个有
- `easy imageScaleDown` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
