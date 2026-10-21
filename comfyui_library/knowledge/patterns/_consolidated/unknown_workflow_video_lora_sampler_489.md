---
name: unknown_workflow_video_lora_sampler_489
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.73875
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, GetNode, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3PromptEnhancerT8, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, SetNode, T8LLMProviderConfig, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Daiswa_双图参考（API调用）_2108442503518179330.json, 视频生成/图生视频/Dasiwa-V2-参考生视频（API调用）_2108746479836950529.json, 视频生成/图生视频/Minimax-h3_图生视频（API调用版本）_2108740302222741506.json, 视频生成/图生视频/Minimax-h3_图生视频（二采放大）_2100102538916880386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_489

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Daiswa_双图参考（API调用）_2108442503518179330.json、视频生成/图生视频/Dasiwa-V2-参考生视频（API调用）_2108746479836950529.json、视频生成/图生视频/Minimax-h3_图生视频（API调用版本）_2108740302222741506.json、视频生成/图生视频/Minimax-h3_图生视频（二采放大）_2100102538916880386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3PromptEnhancerT8`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `T8LLMProviderConfig`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `SaveLatent` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `Any To String (mtb)` —— 2/4 个有
- `AudioCrop` —— 2/4 个有
- `LTXVAudioVAEEncode` —— 2/4 个有
- `LTXVConcatAVLatent` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `SaveAudioAdvanced` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有
- `Int` —— 1/4 个有
- `SaveAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
