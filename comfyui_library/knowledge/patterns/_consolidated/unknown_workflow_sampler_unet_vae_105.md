---
name: unknown_workflow_sampler_unet_vae_105
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.840909
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100405446006890498.json, 平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json, 平台全量/【MINIMAX-H3教学】SelfLift二采_2117192175418175490.json, 平台全量/【MINIMAX-H3教学】SelfLift二采（低显存兼容）_2117222656276783106.json, 视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json, 视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json, 视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json, 视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_105

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100405446006890498.json、平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json、平台全量/【MINIMAX-H3教学】SelfLift二采_2117192175418175490.json、平台全量/【MINIMAX-H3教学】SelfLift二采（低显存兼容）_2117222656276783106.json、视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `MiniMaxChunkFeedForward` —— 9/11 个有
- `MiniMaxLowVRAMAttention` —— 9/11 个有
- `ModelPreviewOverrideKJ` —— 9/11 个有
- `H3SigmaRefiner` —— 8/11 个有
- `MiniMaxH3ReferenceToVideo` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `MiniMaxH3SigmaShift` —— 6/11 个有
- `SelfLiftAvatarH3Sampler` —— 6/11 个有
- `easy seed` —— 6/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `SelfLiftH3Sampler` —— 5/11 个有
- `LoadAudio` —— 4/11 个有
- `JWInteger` —— 3/11 个有
- `MiniMaxH3TurboLoRA` —— 3/11 个有
- `RH_Astra` —— 3/11 个有
- `SaveVideoNode` —— 3/11 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `BlockSparseAttention` —— 2/11 个有
- `Int` —— 2/11 个有
- `LoraLoaderBypassModelOnly` —— 2/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
