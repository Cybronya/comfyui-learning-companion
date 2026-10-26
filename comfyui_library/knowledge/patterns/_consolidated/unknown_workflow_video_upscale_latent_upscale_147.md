---
name: unknown_workflow_video_upscale_latent_upscale_147
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6695
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, DisableNoise, ExtendIntermediateSigmas, GetNode, GoohaiUniversalSlider, ImageScaleToTotalPixels, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudioUI, LoadImage, LoadVideoUI, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy float, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3_三采最强工作流_视频无缝续接_2113816891000188929.json, 视频生成/图生视频/Minimax H3_三采最强工作流_音频驱动_2113272320948260865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_147

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax H3_三采最强工作流_视频无缝续接_2113816891000188929.json、视频生成/图生视频/Minimax H3_三采最强工作流_音频驱动_2113272320948260865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `DisableNoise`
- `ExtendIntermediateSigmas`
- `GetNode`
- `GoohaiUniversalSlider`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudioUI`
- `LoadImage`
- `LoadVideoUI`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `MiniMaxH3MotionContext` —— 1/2 个有
- `MiniMaxH3MotionContextTrim` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
