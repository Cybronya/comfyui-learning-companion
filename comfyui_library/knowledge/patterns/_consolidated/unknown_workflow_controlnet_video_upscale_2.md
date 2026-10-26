---
name: unknown_workflow_controlnet_video_upscale_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.852
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CheckpointLoaderSimple, ComfyMathExpression, DA3Inference, DA3Render, GetImageSize, ImageBlend, ImageConcatMulti, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadDA3Model, LoadImage, LoraLoaderModelOnly, MMH3LatentUpscaleWithModelParams, MMH3TemporalSplitParams, MMH3UltimateUpscale, MiniMaxChunkFeedForward, MiniMaxH3FunControlNetApply, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPatchLoader, ModelPreviewOverrideKJ, PrimitiveInt, PrimitiveStringMultiline, QwenH3PromptLocal, RTDETR_detect, RandomNoise, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SamplerCustomAdvanced, SetLatentNoiseMask, ShowText|pysssss, SolidMask, UNETLoader, VAEDecode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy positive, easy showAnything, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻！！！单人_2113798284304277506.json, 视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻（单人）_2108499578348720130.json, 视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻（单人）_2108528269028052994.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻！！！单人_2113798284304277506.json、视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻（单人）_2108499578348720130.json、视频生成/图生视频/1-Aiden-人物动作迁移，表情及口型复刻（单人）_2108528269028052994.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DA3Inference`
- `DA3Render`
- `GetImageSize`
- `ImageBlend`
- `ImageConcatMulti`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadDA3Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MMH3LatentUpscaleWithModelParams`
- `MMH3TemporalSplitParams`
- `MMH3UltimateUpscale`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3FunControlNetApply`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPatchLoader`
- `ModelPreviewOverrideKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenH3PromptLocal`
- `RTDETR_detect`
- `RandomNoise`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy positive`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
