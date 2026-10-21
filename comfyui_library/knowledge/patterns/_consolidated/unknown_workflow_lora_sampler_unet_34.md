---
name: unknown_workflow_lora_sampler_unet_34
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9368
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RH_DLSS5FrameInterpolation, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 2K_2098776214440865793.json, 视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 4K_2098689766622580737.json, 视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 768P_2098689834578698241.json, 视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 2K_2098776208187154433.json, 视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 4K_2098400619433381889.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 2K_2098776214440865793.json、视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 4K_2098689766622580737.json、视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 768P_2098689834578698241.json、视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 2K_2098776208187154433.json、视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 4K_2098400619433381889.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_DLSS5FrameInterpolation`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `SeedVR2` —— 4/5 个有
- `SeedVR2BlockSwap` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `MiniMaxChunkFeedForward` —— 3/5 个有
- `MiniMaxLowVRAMAttention` —— 3/5 个有
- `SelfLiftH3Sampler` —— 3/5 个有
- `BasicGuider` —— 2/5 个有
- `LTXVConcatAVLatent` —— 2/5 个有
- `LTXVSeparateAVLatent` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `MinimaxH3LatentUpscaler3D` —— 2/5 个有
- `RandomNoise` —— 2/5 个有
- `SamplerCustomAdvanced` —— 2/5 个有
- `SplitSigmas` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
