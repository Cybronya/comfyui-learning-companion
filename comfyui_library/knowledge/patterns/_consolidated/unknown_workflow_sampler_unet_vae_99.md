---
name: unknown_workflow_sampler_unet_vae_99
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.814
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/老王房产专用流-Minimax+H3双模双采_2097619417130684417.json, 视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json, 视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json, 视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json, 视频生成/图生视频/同模双采 H3 动态修复_2096940486610219009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_99

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/老王房产专用流-Minimax+H3双模双采_2097619417130684417.json、视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json、视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json、视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
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
- `H3SigmaRefiner` —— 6/7 个有
- `LTXVConcatAVLatent` —— 6/7 个有
- `LTXVSeparateAVLatent` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 6/7 个有
- `SplitSigmas` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `MiniMaxH3TurboLoRA` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `MiniMaxLowVRAMAttention` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `SolAttnMiniMax` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `ConcatTextOfUtils` —— 2/7 个有
- `MiniMaxChunkFeedForward` —— 2/7 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/7 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/7 个有
- `Astra` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/7 个有
- `MiniMaxH3VAEDecodeFast` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
