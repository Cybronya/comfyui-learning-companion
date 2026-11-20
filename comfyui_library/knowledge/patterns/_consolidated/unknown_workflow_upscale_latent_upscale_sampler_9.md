---
name: unknown_workflow_upscale_latent_upscale_sampler_9
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8644
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json, 视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json, 视频生成/图生视频/minMax+H3+二采放大_2091513919167885314.json, 视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json, 视频生成/图生视频/minimax h3_ref2va-dasiwa-zs05可选双采_2092257046572920834.json, 视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json, 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json, 视频生成/图生视频/【合理动态版】Hybrid_4+5步双采样_2096530913504088066.json, 视频生成/图生视频/【疯了的动态】Dasiwa_4+5步双采样_2096866880698015746.json, 视频生成/图生视频/黄色的大宝剑武打流放大二采_2109571702479998978.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json、视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json、视频生成/图生视频/minMax+H3+二采放大_2091513919167885314.json、视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json、视频生成/图生视频/minimax h3_ref2va-dasiwa-zs05可选双采_2092257046572920834.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `ModelAttentionBackend` —— 8/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `SplitSigmas` —— 7/10 个有
- `ManualSigmas` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `CreateVideo` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `LoraLoaderBypassModelOnly` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `BlockSparseAttention` —— 2/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `LoadAudio` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
