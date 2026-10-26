---
name: unknown_workflow_sampler_unet_vae_111
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.736333
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json, 视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json, 视频生成/图生视频/MiniMax H3 黑科技加速双采-self-lift工作流_2098836942896062465.json, 视频生成/图生视频/Minimax H3 + Self-lift双采快速超长工作流_2104549240100970498.json, 视频生成/图生视频/Minimax H3 最佳动作视频生成 Ref2V 工作流_2112874707992276993.json, 视频生成/图生视频/qwen文武_2113903502299852801.json, 视频生成/图生视频/qwen文武_2113913807365033985.json, 视频生成/图生视频/改至YZ金鱼-MiniMax H3 终极篇-文武双全_2111027801062203393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_111

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json、视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json、视频生成/图生视频/MiniMax H3 黑科技加速双采-self-lift工作流_2098836942896062465.json、视频生成/图生视频/Minimax H3 + Self-lift双采快速超长工作流_2104549240100970498.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelAttentionBackend` —— 8/9 个有
- `SelfLiftH3Sampler` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `H3SigmaRefiner` —— 6/9 个有
- `MiniMaxH3SigmaShift` —— 6/9 个有
- `BlockSparseAttention` —— 5/9 个有
- `MiniMaxChunkFeedForward` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `LoadAudio` —— 4/9 个有
- `SaveVideo` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `Text` —— 4/9 个有
- `忽略多组孤海` —— 4/9 个有
- `GetNode` —— 3/9 个有
- `MiniMaxLowVRAMAttention` —— 3/9 个有
- `QwenH3PromptLocal` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `GoohaiUniversalSlider` —— 2/9 个有
- `SelfLiftAvatarH3Sampler` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/9 个有
- `easy loraStack` —— 1/9 个有
- `easy loraStackApply` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
