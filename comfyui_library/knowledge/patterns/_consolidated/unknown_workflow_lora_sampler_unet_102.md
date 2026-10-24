---
name: unknown_workflow_lora_sampler_unet_102
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.879429
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json, 视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json, 视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 2K_2098776214440865793.json, 视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 4K_2098689766622580737.json, 视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 768P_2098689834578698241.json, 视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 2K_2098776208187154433.json, 视频生成/文生视频/MiniMax H3｜Sigma强化双采｜通用生视频 4K_2098400619433381889.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json、视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json、视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 2K_2098776214440865793.json、视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 4K_2098689766622580737.json、视频生成/文生视频/MiniMax H3｜SelfLift｜通用生视频 768P_2098689834578698241.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `ModelPreviewOverrideKJ` —— 5/7 个有
- `RH_DLSS5FrameInterpolation` —— 5/7 个有
- `SelfLiftH3Sampler` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `Int` —— 4/7 个有
- `LTXVSeparateAVLatent` —— 4/7 个有
- `SeedVR2` —— 4/7 个有
- `SeedVR2BlockSwap` —— 4/7 个有
- `MiniMaxChunkFeedForward` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `BasicGuider` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
