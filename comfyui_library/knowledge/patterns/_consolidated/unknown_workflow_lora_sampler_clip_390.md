---
name: unknown_workflow_lora_sampler_clip_390
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, DisableNoise, ExtendIntermediateSigmas, KSamplerSelect, LLAIDownloadVideo, LoadAudio, LoadImage, LoadVideoUI, LoraLoaderModelOnly, MiniMaxH3LoadLatent, MiniMaxH3ReferenceToVideo, MiniMaxH3SaveLatent, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SigmaShift, MiniMaxH3SparkAttentionAuto, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, SplitSigmasDenoise, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/多参模式工作流第1弹｜文图视频三模输入全能参考生成_2114684100194947074.json, 视频生成/视频生视频/多参模式 (1)_2092890652542595073.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_390

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/多参模式工作流第1弹｜文图视频三模输入全能参考生成_2114684100194947074.json、视频生成/视频生视频/多参模式 (1)_2092890652542595073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DisableNoise`
- `ExtendIntermediateSigmas`
- `KSamplerSelect`
- `LLAIDownloadVideo`
- `LoadAudio`
- `LoadImage`
- `LoadVideoUI`
- `LoraLoaderModelOnly`
- `MiniMaxH3LoadLatent`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SaveLatent`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3SparkAttentionAuto`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `SplitSigmasDenoise`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ContextLatentTaperNoise` —— 1/2 个有
- `MiniMaxH3MotionContext` —— 1/2 个有
- `MiniMaxH3MotionContextTrim` —— 1/2 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 1/2 个有
- `MiniMaxH3VideoExtender` —— 1/2 个有
- `SolAttnMiniMax` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
