---
name: unknown_workflow_video_lora_sampler_864
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.678
common_nodes: [BasicScheduler, CLIPLoader, GetNode, JjkText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json, 视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_864

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json、视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `Int` —— 1/2 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `QwenH3PromptLocal` —— 1/2 个有
- `T8LLMProviderConfig` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
