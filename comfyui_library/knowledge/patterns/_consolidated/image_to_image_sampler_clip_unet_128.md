---
name: image_to_image_sampler_clip_unet_128
type: Image To Image
frequency: 5
level: strong
coverage: 0.9666
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/clein 溶图工作流_2052269296637755394.json, 图片生成/文生图/毛坯转效果图-室内设计专用-Flux2-klein_2012839162801557505.json, 平台全量/Flux2-Klein-图片编辑 (单图)_2057746502453387265.json, 平台全量/Flux2-klein多图编辑_2012307550632419329.json, 平台全量/Flux2-klein扩图_2013051242397831170.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/clein 溶图工作流_2052269296637755394.json、图片生成/文生图/毛坯转效果图-室内设计专用-Flux2-klein_2012839162801557505.json、平台全量/Flux2-Klein-图片编辑 (单图)_2057746502453387265.json、平台全量/Flux2-klein多图编辑_2012307550632419329.json、平台全量/Flux2-klein扩图_2013051242397831170.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PIP_图像联结` —— 3/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `LayerMask: ImageToMask` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
