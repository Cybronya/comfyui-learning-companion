---
name: image_to_image_lora_sampler_unet_42
type: Image To Image
frequency: 14
level: strong
coverage: 0.746857
common_nodes: [CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyImage, GetImageSize, GrowMask, ImageCompositeMasked, ImageFromBatch, ImageResizeKJv2, InvertMask, KSampler, LTXVConcatAVLatent, LoadBackgroundRemovalModel, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, RemoveBackground, ResizeImageMaskNode, ResolutionSelector, SaveVideo, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Minimax H3 角色替换_2090420332376186882.json, 平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json, 平台全量/Minimax H3+sec4B角色替换_2090037412381683713.json, 平台全量/Minimax H3+sec4B角色替换_2090340234662866945.json, 平台全量/Minimax H3+sec4B角色替换_2094780121004724225.json, 平台全量/Minimax H3+sec4B角色替换（手动打点遮罩）_2095151665283428353.json, 平台全量/Minimax H3+sec4B角色遮罩替换_2090352291864997889.json, 数字人/数字人/海螺H3！Sec定点遮罩替换_2092136875254439938.json, 数字人/数字人/视频指定人物替换 Minimax H3  - SEC_2092432088149610498.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2090226018845024258.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2109443531659104257.json, 视频生成/图生视频/Minimax H3+sec4B角色替换_2110274068917342210.json, 视频生成/图生视频/Minimax+H3+局部编辑_2090659815860297729.json, 视频生成/图生视频/Minimax_H3+sec4B角色遮罩替换_2116336005165969410.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/Minimax H3 角色替换_2090420332376186882.json、平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json、平台全量/Minimax H3+sec4B角色替换_2090037412381683713.json、平台全量/Minimax H3+sec4B角色替换_2090340234662866945.json、平台全量/Minimax H3+sec4B角色替换_2094780121004724225.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `GetImageSize`
- `GrowMask`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `InvertMask`
- `KSampler`
- `LTXVConcatAVLatent`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RemoveBackground`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveVideo`
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
- `PointsEditor` —— 13/14 个有
- `PreviewAnimation` —— 13/14 个有
- `SeCModelLoader` —— 13/14 个有
- `SeCVideoSegmentation` —— 13/14 个有
- `ImageBlend` —— 12/14 个有
- `MaskToImage` —— 12/14 个有
- `GetNode` —— 11/14 个有
- `ImageStitch` —— 11/14 个有
- `SetNode` —— 11/14 个有
- `PreviewImage` —— 10/14 个有
- `VHS_VideoCombine` —— 3/14 个有
- `JjkText` —— 2/14 个有
- `CLIPTextEncode` —— 1/14 个有
- `CheckpointLoaderSimple` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `Int` —— 1/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/14 个有
- `PathchSageAttentionKJ` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `SAM3_TrackEditMask` —— 1/14 个有
- `SAM3_VideoTrack` —— 1/14 个有
- `SCAIL2ColoredMaskV2` —— 1/14 个有
- `easy sam3ModelLoader` —— 1/14 个有
- `easy sam3VideoSegmentation` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 14 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，14 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
