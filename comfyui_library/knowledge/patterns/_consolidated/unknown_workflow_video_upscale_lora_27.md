---
name: unknown_workflow_video_upscale_lora_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7875
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, ConcatTextOfUtils, GetNode, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ChunkedTwoPassPlanT8Advanced, MiniMaxH3ChunkedTwoPassUpscaleT8Advanced, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, ShellAgentPluginVideoCombineEncrypt, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/20s+MinimaxH3+LMS+同模双采+语义桥+分块采样（声音有瑕疵）_2100942119115509761.json, 视频生成/图生视频/20s+音频驱动分块-语义桥-MiniMax+H3参考生视频_2100942144549773313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/20s+MinimaxH3+LMS+同模双采+语义桥+分块采样（声音有瑕疵）_2100942119115509761.json、视频生成/图生视频/20s+音频驱动分块-语义桥-MiniMax+H3参考生视频_2100942144549773313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConcatTextOfUtils`
- `GetNode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced`
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `ShellAgentPluginVideoCombineEncrypt`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3AudioConditioningT8` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
