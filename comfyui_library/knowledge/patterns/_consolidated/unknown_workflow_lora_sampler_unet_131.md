---
name: unknown_workflow_lora_sampler_unet_131
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.795167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json, 视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json, 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json, 视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json, 视频生成/图生视频/minimaxh3的selflift+二采+音频参考_2105937177262772225.json, 视频生成/文生视频/minimaxh3的selflift+二采_2101192695308963842.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_131

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json、视频生成/图生视频/Minimax H3-lightx2v不同版加速lora测试_2096422700070817794.json、视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json、视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json、视频生成/图生视频/minimaxh3的selflift+二采+音频参考_2105937177262772225.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `LTXVConcatAVLatent` —— 5/6 个有
- `LTXVSeparateAVLatent` —— 5/6 个有
- `MinimaxH3LatentUpscaler3D` —— 5/6 个有
- `ModelPreviewOverrideKJ` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `H3SigmaRefiner` —— 4/6 个有
- `MiniMaxChunkFeedForward` —— 4/6 个有
- `MiniMaxLowVRAMAttention` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `AddLabel` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `PlaySound|pysssss` —— 2/6 个有
- `SelfLiftAvatarH3Sampler` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `MiniMaxH3BlockCacheT8` —— 1/6 个有
- `SelfLiftH3Sampler` —— 1/6 个有
- `SolAttnMiniMax` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
