---
name: unknown_workflow_lora_sampler_unet_4
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.746
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json, 视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json, 视频生成/图生视频/Minimax-h3-多参视频生成（不油、不偏色及一致性好）_2107461072583221250.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2099777362543075329.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2100037395591815170.json, 视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json, 视频生成/图生视频/minimaxh3的selflift+二采+音频参考_2105937177262772225.json, 视频生成/图生视频/（修脸极速）黑科技加速minimax h3 self-lift双采多参生视频_2098223404263497730.json, 视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json, 视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json, 视频生成/文生视频/MiniMax H3 二采去油不爆音加速工作流_2096198192596606977.json, 视频生成/文生视频/minimaxh3的selflift+二采_2101192695308963842.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json、视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json、视频生成/图生视频/Minimax-h3-多参视频生成（不油、不偏色及一致性好）_2107461072583221250.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 13/14 个有
- `ModelPreviewOverrideKJ` —— 12/14 个有
- `ConditioningZeroOut` —— 10/14 个有
- `H3SigmaRefiner` —— 10/14 个有
- `PrimitiveStringMultiline` —— 10/14 个有
- `VHS_VideoCombine` —— 10/14 个有
- `CreateVideo` —— 9/14 个有
- `SelfLiftH3Sampler` —— 8/14 个有
- `BasicGuider` —— 6/14 个有
- `GetNode` —— 6/14 个有
- `RandomNoise` —— 6/14 个有
- `SamplerCustomAdvanced` —— 6/14 个有
- `SetNode` —— 6/14 个有
- `LoadAudio` —— 5/14 个有
- `SaveVideo` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `LTXVConcatAVLatent` —— 3/14 个有
- `LTXVSeparateAVLatent` —— 3/14 个有
- `MinimaxH3LatentUpscaler3D` —— 3/14 个有
- `VHS_LoadVideo` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `PlaySound|pysssss` —— 2/14 个有
- `SelfLiftAvatarH3Sampler` —— 2/14 个有
- `easy float` —— 2/14 个有
- `GetImageRangeFromBatch` —— 1/14 个有
- `MiniMaxH3AddGuide` —— 1/14 个有
- `MiniMaxH3ImageToVideo` —— 1/14 个有
- `MiniMaxH3TurboSampler` —— 1/14 个有
- `SplitSigmas` —— 1/14 个有
- `Text` —— 1/14 个有
- `TrimAudioDuration` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
