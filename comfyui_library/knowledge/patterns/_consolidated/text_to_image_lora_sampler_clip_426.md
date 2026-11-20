---
name: text_to_image_lora_sampler_clip_426
type: Text To Image
frequency: 5
level: strong
coverage: 0.741
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyImage, EmptyLatentImage, GetImageSize, GetNode, GrowMask, ImageBlend, ImageCompositeMasked, ImageFromBatch, ImageResizeKJv2, ImageStitch, InvertMask, JjkText, KSampler, LTXVConcatAVLatent, LoadBackgroundRemovalModel, LoadImage, LoraLoaderModelOnly, MaskToImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PointsEditor, PreviewAnimation, PreviewImage, RemoveBackground, ResizeImageMaskNode, ResolutionSelector, SaveVideo, SeCModelLoader, SeCVideoSegmentation, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/sec4B角色遮罩替换｜Minimax H3视频人物替换生成_2090849503518748674.json, 平台全量/角色一键替换｜Minimax H3视频生视频创意生成_2091196655000440834.json, 视频生成/图生视频/Minimax H3+sec4B角色替换｜动漫角色人物特效图生视频_2110768716433682433.json, 视频生成/图生视频/Minimax H3加sec4B角色替换 一键换人视频方案_2110249048413396993.json, 视频生成/图生视频/Minimax H3加sec4B角色替换 一键换人视频方案_2110364239595659265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_426

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/sec4B角色遮罩替换｜Minimax H3视频人物替换生成_2090849503518748674.json、平台全量/角色一键替换｜Minimax H3视频生视频创意生成_2091196655000440834.json、视频生成/图生视频/Minimax H3+sec4B角色替换｜动漫角色人物特效图生视频_2110768716433682433.json、视频生成/图生视频/Minimax H3加sec4B角色替换 一键换人视频方案_2110249048413396993.json、视频生成/图生视频/Minimax H3加sec4B角色替换 一键换人视频方案_2110364239595659265.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageStitch`
- `InvertMask`
- `JjkText`
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
- `PreviewImage`
- `RemoveBackground`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveVideo`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
