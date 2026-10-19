---
name: unknown_workflow_video_lora_sampler_751
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, EasyCache, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3加速方式对比_2087392191630106625.json, 视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_751

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3加速方式对比_2087392191630106625.json、视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EasyCache`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `SolAttnMiniMax` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `easy string` —— 1/2 个有
- `string_util_StrConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
