---
name: unknown_workflow_video_upscale_latent_upscale_86
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.413
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy float, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/2采五段加速流_2104580181368336385.json, 视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！_2107500379746430977.json, 视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！加放大_2110238781872889857.json, 视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_86

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2采五段加速流_2104580181368336385.json、视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！_2107500379746430977.json、视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！加放大_2110238781872889857.json、视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 3/4 个有
- `AudioConcat` —— 2/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `MiniMaxH3AddGuide` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `TrimAudioDuration` —— 2/4 个有
- `BlockSparseAttention` —— 1/4 个有
- `GH_AudioVideoMerger` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LayerColor: ColorAdapter` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
