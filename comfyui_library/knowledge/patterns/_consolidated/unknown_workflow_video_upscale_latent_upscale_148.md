---
name: unknown_workflow_video_upscale_latent_upscale_148
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.861
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ComfySwitchNode, ImageBatchMulti, ImageFromBatch, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MiniMaxH3ChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveInt, RandomNoise, RepeatImageBatch, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VRAMReserver, easy cleanGpuUsed, easy loraStack, easy loraStackApply, easy positive]
problems: []
missing: []
members: [平台全量/minimax h3 Pika 动作迁移_人物替换_原2采版本快_2119047176184745985.json, 平台全量/minimax h3 动作迁移_人物替换_原2采版本快_2115708699674234882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/minimax h3 Pika 动作迁移_人物替换_原2采版本快_2119047176184745985.json、平台全量/minimax h3 动作迁移_人物替换_原2采版本快_2115708699674234882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ImageBatchMulti`
- `ImageFromBatch`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `RepeatImageBatch`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy loraStack`
- `easy loraStackApply`
- `easy positive`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
