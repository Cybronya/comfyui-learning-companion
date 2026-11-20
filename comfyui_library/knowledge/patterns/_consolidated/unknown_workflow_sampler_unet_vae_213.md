---
name: unknown_workflow_sampler_unet_vae_213
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.862857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json, 视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json, 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json, 视频生成/图生视频/同模双采 H3 动态修复_2096940486610219009.json, 视频生成/文生视频/Minimax H3优化！浅空间二次放大！优化小脸和打斗_2087552804436140033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_213

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json、视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json、视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 6/7 个有
- `LTXVSeparateAVLatent` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 6/7 个有
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SplitSigmas` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `MiniMaxH3TurboLoRA` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 3/7 个有
- `AddLabel` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `ManualSigmas` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `SelfLiftH3Sampler` —— 1/7 个有
- `SolAttnMiniMax` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
