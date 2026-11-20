---
name: unknown_workflow_lora_sampler_unet_111
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.821714
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, ExtendIntermediateSigmas, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2108808210898579458.json, 视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2110214146649321474.json, 视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2110281194754629633.json, 视频生成/图生视频/MiniMax H3-SelfLift-加速双采-武戏动态强-参考生视频_2107869504612163586.json, 视频生成/图生视频/MiniMax_H3-SelfLift-加速双采-武戏动态强-参考生视频_2110654582593507330.json, 视频生成/文生视频/H3-双采_2097870437538680834.json, 视频生成/文生视频/MiniMax H3-SelfLift-加速双采-文戏不油，武戏动态强-参考生视频_2101227963210625025.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_111

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2108808210898579458.json、视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2110214146649321474.json、视频生成/图生视频/MiniMax H3-SelfLift-加速双采+单采-参考生视频_2110281194754629633.json、视频生成/图生视频/MiniMax H3-SelfLift-加速双采-武戏动态强-参考生视频_2107869504612163586.json、视频生成/图生视频/MiniMax_H3-SelfLift-加速双采-武戏动态强-参考生视频_2110654582593507330.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `ExtendIntermediateSigmas`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/7 个有
- `RandomNoise` —— 5/7 个有
- `SamplerCustomAdvanced` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `Any Switch (rgthree)` —— 4/7 个有
- `Fast Groups Muter (rgthree)` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `SolAttnMiniMax` —— 3/7 个有
- `BlockSparseAttention` —— 2/7 个有
- `ImageScale` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `ManualSigmas` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
