---
name: unknown_workflow_sampler_unet_vae_198
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.807667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), KSamplerSelect, Label (rgthree), LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 全模态视频生成 I 提示词强化 I 超分_2084660524603764738.json, 视频生成/文生视频/MiniMax H3 全能大合集工作流_2084920689999572993.json, 视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_198

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 全模态视频生成 I 提示词强化 I 超分_2084660524603764738.json、视频生成/文生视频/MiniMax H3 全能大合集工作流_2084920689999572993.json、视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 2/3 个有
- `MiniMaxH3GenerationTailLoader` —— 2/3 个有
- `MiniMaxH3PromptEnhancer` —— 2/3 个有
- `RTXVideoSuperResolution` —— 2/3 个有
- `VHS_LoadAudioUpload` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxH3HybridLoader` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2ExtraArgs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
