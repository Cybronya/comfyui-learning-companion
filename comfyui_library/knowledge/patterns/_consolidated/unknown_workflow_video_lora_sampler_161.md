---
name: unknown_workflow_video_lora_sampler_161
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.816
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3VAEDecodeFast, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, QwenH3PromptLocal, ResolutionSelector, RunningHub Deepcleaner, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/123_2107820492894855170.json, 视频生成/图生视频/CGDselflift+2xVAE+锐化放大模型工作流_2110638154041618433.json, 视频生成/图生视频/MiniMax H3_selflift+2xVAE+锐化放大工作流_2105110415595364353.json, 视频生成/图生视频/Minimax-H3_2109624727416430594.json, 视频生成/图生视频/MinimaxH3-图生视频-高清2K_2105896544250720257.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104877137932148737.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104929413359030273.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2104933693600129025.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2110566290069999618.json, 视频生成/图生视频/selflift+2xVAE+锐化放大模型工作流_2111010022284161026.json, 视频生成/图生视频/锐化工作流_2113864371016392706.json, 视频生成/文生视频/MimaxH3锐化高清放大采样工作流_2105086382539624449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_161

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/123_2107820492894855170.json、视频生成/图生视频/CGDselflift+2xVAE+锐化放大模型工作流_2110638154041618433.json、视频生成/图生视频/MiniMax H3_selflift+2xVAE+锐化放大工作流_2105110415595364353.json、视频生成/图生视频/Minimax-H3_2109624727416430594.json、视频生成/图生视频/MinimaxH3-图生视频-高清2K_2105896544250720257.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3VAEDecodeFast`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `QwenH3PromptLocal`
- `ResolutionSelector`
- `RunningHub Deepcleaner`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 10/12 个有
- `VAEDecode` —— 9/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `ImageFromBatch` —— 8/12 个有
- `JjkText` —— 2/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
