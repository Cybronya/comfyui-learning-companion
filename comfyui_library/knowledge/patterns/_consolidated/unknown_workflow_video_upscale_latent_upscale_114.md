---
name: unknown_workflow_video_upscale_latent_upscale_114
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, ComfyMathExpression, ConditioningZeroOut, FloatConstant, INTConstant, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MMH3TemporalSplitParams, MMH3UltimateUpscale, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SolAttnMiniMax, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/低显存优化流（时间分块）（孤海3）_2108777093361389570.json, 视频生成/文生视频/低显存优化流（时间分块）（孤海3）_2108777093361389570.json, 视频生成/文生视频/低显存优化流（时间分块）（孤海）_2108578844885209090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_114

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/低显存优化流（时间分块）（孤海3）_2108777093361389570.json、视频生成/文生视频/低显存优化流（时间分块）（孤海3）_2108777093361389570.json、视频生成/文生视频/低显存优化流（时间分块）（孤海）_2108578844885209090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `FloatConstant`
- `INTConstant`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MMH3TemporalSplitParams`
- `MMH3UltimateUpscale`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SolAttnMiniMax`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `H3KitSemanticBridge` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
