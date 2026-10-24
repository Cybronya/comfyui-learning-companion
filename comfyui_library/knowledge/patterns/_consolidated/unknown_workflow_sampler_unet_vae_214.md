---
name: unknown_workflow_sampler_unet_vae_214
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9258
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json, 视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json, 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json, 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_214

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json、视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json、视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json、视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双加速实验）工作流_2094784005777481730.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LTXVConcatAVLatent` —— 4/5 个有
- `LTXVSeparateAVLatent` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `MinimaxH3LatentUpscaler3D` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `SplitSigmas` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `H3SigmaRefiner` —— 3/5 个有
- `MiniMaxH3SigmaShift` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `MiniMaxH3TurboLoRA` —— 2/5 个有
- `MiniMaxLowVRAMAttention` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `MiniMaxChunkFeedForward` —— 1/5 个有
- `SelfLiftH3Sampler` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
