---
name: unknown_workflow_upscale_latent_upscale_sampler_16
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.773833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/minimaxh3-多参+latent二采_2090316749035106305.json, 图片生成/文生图/啊癫 minimaxh3极速版二采潜空间直接放大_2091125688710553601.json, 数字人/数字人/老王房产专用流-Minimax+H3双模双采_2097619417130684417.json, 视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json, 视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/minimaxh3-多参+latent二采_2090316749035106305.json、图片生成/文生图/啊癫 minimaxh3极速版二采潜空间直接放大_2091125688710553601.json、数字人/数字人/老王房产专用流-Minimax+H3双模双采_2097619417130684417.json、视频生成/图生视频/4k+二采新condition+同模双采+H3+动态修复_2108509040342028289.json、视频生成/图生视频/LMS测试+二采新condition+同模双采+语义桥_2100942089772163074.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `MiniMaxLowVRAMAttention` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `MiniMaxH3TurboLoRA` —— 3/6 个有
- `Seed (rgthree)` —— 3/6 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 3/6 个有
- `SolAttnMiniMax` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `ConcatTextOfUtils` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/6 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/6 个有
- `Astra` —— 1/6 个有
- `ExtendIntermediateSigmas` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/6 个有
- `MiniMaxH3VAEDecodeFast` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
