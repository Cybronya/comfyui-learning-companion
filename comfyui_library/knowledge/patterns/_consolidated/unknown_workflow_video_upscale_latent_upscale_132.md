---
name: unknown_workflow_video_upscale_latent_upscale_132
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.595
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3社区模型工作流高质量加速版-0902_2087768558020423681.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏(修改版）_2103351056783728641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_132

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3社区模型工作流高质量加速版-0902_2087768558020423681.json、视频生成/图生视频/【MINIMAX-H3】八月最强文戏(修改版）_2103351056783728641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `MiniMaxH3Easy` —— 1/2 个有
- `MiniMaxH3EasyLoader` —— 1/2 个有
- `MiniMaxH3EasyOutput` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
