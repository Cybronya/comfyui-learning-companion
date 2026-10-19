---
name: image_to_image_lora_sampler_unet_5
type: Image To Image
frequency: 6
level: strong
coverage: 0.7285
common_nodes: [CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyImage, GetImageSize, GrowMask, ImageBlend, ImageCompositeMasked, ImageFromBatch, ImageResizeKJv2, InvertMask, KSampler, LTXVConcatAVLatent, LoadBackgroundRemovalModel, LoadImage, LoraLoaderModelOnly, MaskToImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PointsEditor, PreviewAnimation, RemoveBackground, ResizeImageMaskNode, ResolutionSelector, SaveVideo, SeCModelLoader, SeCVideoSegmentation, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/海螺H3！Sec定点遮罩替换_2092136875254439938.json, 数字人/数字人/视频指定人物替换 Minimax H3  - SEC_2092432088149610498.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2090226018845024258.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2109443531659104257.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2110274068917342210.json, 视频生成/图生视频/Minimax+H3+局部编辑_2090659815860297729.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/海螺H3！Sec定点遮罩替换_2092136875254439938.json、数字人/数字人/视频指定人物替换 Minimax H3  - SEC_2092432088149610498.json、视频生成/图生视频/Minimax H3+sec4B角色替换_2090226018845024258.json、视频生成/图生视频/Minimax H3+sec4B角色替换_2109443531659104257.json、视频生成/图生视频/Minimax H3+sec4B角色替换_2110274068917342210.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `GetImageSize`
- `GrowMask`
- `ImageBlend`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `InvertMask`
- `KSampler`
- `LTXVConcatAVLatent`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PointsEditor`
- `PreviewAnimation`
- `RemoveBackground`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveVideo`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `ImageStitch` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `JjkText` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有
- `easy sam3VideoSegmentation` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 6 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
