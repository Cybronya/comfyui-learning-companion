---
name: unknown_workflow_sampler_unet_vae_141
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.487222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 双采样 潜空间放大DSW（二次优化）_2095748408920330241.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大_2090792067181137921.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大（二次优化）_2091136885820313602.json, 视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json, 视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089663075422130178.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089687254284455937.json, 视频生成/图生视频/h3潜空间放大工作流老八_2089878151064276994.json, 视频生成/图生视频/二采-10s(768P→1080p) Minimax多参生视频_2090054499200225281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_141

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 双采样 潜空间放大DSW（二次优化）_2095748408920330241.json、视频生成/图生视频/MiniMax H3 双采样 潜空间放大_2090792067181137921.json、视频生成/图生视频/MiniMax H3 双采样 潜空间放大（二次优化）_2091136885820313602.json、视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json、视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 8/9 个有
- `LTXVSeparateAVLatent` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `SplitSigmas` —— 8/9 个有
- `ModelAttentionBackend` —— 7/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `LTXVConcatAVLatent` —— 5/9 个有
- `MiniMaxH3SigmaShift` —— 5/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 5/9 个有
- `SolAttnMiniMax` —— 5/9 个有
- `Float` —— 4/9 个有
- `ModelPreviewOverrideKJ` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `Text` —— 4/9 个有
- `CreateVideo` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `MinimaxH3LatentUpscaler3D` —— 3/9 个有
- `PT_H3ConcatAVLatent` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LoraLoaderBypassModelOnly` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/9 个有
- `MiniMaxH3HybridLoader` —— 1/9 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/9 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/9 个有
- `MiniMaxH3TurboLoRA` —— 1/9 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
