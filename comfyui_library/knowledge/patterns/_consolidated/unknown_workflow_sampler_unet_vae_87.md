---
name: unknown_workflow_sampler_unet_vae_87
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.884375
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json, 视频生成/图生视频/2图参考生视频minimax_2110625760905089026.json, 视频生成/图生视频/2张参考图_2110029532303552514.json, 视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json, 视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json, 视频生成/图生视频/MiniMax H3+lightx2v 4步加速全能参考工作流2图_2086437276707545089.json, 视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json, 视频生成/文生视频/Minimax H3 多参生视频_2087727061006901250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_87

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json、视频生成/图生视频/2图参考生视频minimax_2110625760905089026.json、视频生成/图生视频/2张参考图_2110029532303552514.json、视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json、视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `LoadAudio` —— 5/8 个有
- `ModelAttentionBackend` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxH3BlockCacheT8` —— 2/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/8 个有
- `SpectrumSDXL` —— 2/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `H3AdaLNLoRAFix` —— 1/8 个有
- `LoadImageFromUrl` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `TrimAudioDuration` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
