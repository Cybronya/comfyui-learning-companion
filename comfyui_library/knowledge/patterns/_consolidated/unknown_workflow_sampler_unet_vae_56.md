---
name: unknown_workflow_sampler_unet_vae_56
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.605231
common_nodes: [BasicGuider, CLIPLoader, CM_BoolToInt, CR Prompt Text, ComfyMathExpression, CreateVideo, ExecutionBlocker, FloatToText, GetCurrentTimeNode, ImpactNeg, JjkText, LoadImage, PreviewAny, PrimitiveBoolean, PrimitiveFloat, RHLLMChatNode, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, SaveLatent, SaveVideo, StringReplace, UNETLoader, VAEEncode, VAELoader, easy anythingIndexSwitch, easy mathString, ttN concat, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/10Eros-MiniMax V3 参考生视频_2086459184501051393.json, 视频生成/图生视频/10Eros-MiniMax V3 图生视频8步加速版 自动提示词优化_2087012748470349826.json, 视频生成/图生视频/10Eros-MiniMax V3 图生视频_2086411157291749378.json, 视频生成/图生视频/10Eros-minimax-beta3 双采 参考生视频 latent放大_2092515663633010690.json, 视频生成/图生视频/10Eros-minimax-beta4 latent放大双采样_2093644717547409410.json, 视频生成/图生视频/Dasiwa-MiniMax H3 参考生视频 双采样latent放大_2092552001400958978.json, 视频生成/图生视频/Dasiwa-MiniMax H3+600ema 极佳高动态效果 latent放大双采样_2093644724950364161.json, 视频生成/图生视频/Dasiwa-MiniMax_H3+600ema_极佳高动态效果_latent放大双采样_2102691989845274625.json, 视频生成/图生视频/Dasiwa-MiniMax_H3+600ema_极佳高动态效果_latent放大双采样_2104387680342724609.json, 视频生成/图生视频/Dasiwa-MiniMax_H3+600ema_极佳高动态效果_latent放大双采样_2104750906087657473.json, 视频生成/图生视频/MiniMax H3双采样 图生视频_参考生视频 极速超清_2087754187215032322.json, 视频生成/图生视频/MiniMax H3双采样V2latent放大版_2090390049698435074.json, 视频生成/图生视频/MiniMaxH3双采样latent放大260831_2094432144478269441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_56

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/10Eros-MiniMax V3 参考生视频_2086459184501051393.json、视频生成/图生视频/10Eros-MiniMax V3 图生视频8步加速版 自动提示词优化_2087012748470349826.json、视频生成/图生视频/10Eros-MiniMax V3 图生视频_2086411157291749378.json、视频生成/图生视频/10Eros-minimax-beta3 双采 参考生视频 latent放大_2092515663633010690.json、视频生成/图生视频/10Eros-minimax-beta4 latent放大双采样_2093644717547409410.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CM_BoolToInt`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `ExecutionBlocker`
- `FloatToText`
- `GetCurrentTimeNode`
- `ImpactNeg`
- `JjkText`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `SaveLatent`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy mathString`
- `ttN concat`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 12/13 个有
- `ImageScaleToTotalPixels` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/13 个有
- `ModelAttentionBackend` —— 10/13 个有
- `CM_FloatBinaryOperation` —— 9/13 个有
- `GetNode` —— 9/13 个有
- `LayerUtility: PurgeVRAM` —— 9/13 个有
- `LoraLoaderBypassModelOnly` —— 9/13 个有
- `MiniMaxH3AVDecodeT8` —— 9/13 个有
- `SetNode` —— 9/13 个有
- `MiniMaxH3AudioConditioningT8` —— 8/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 8/13 个有
- `SolAttnMiniMax` —— 8/13 个有
- `IntConditions` —— 7/13 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 7/13 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 7/13 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 7/13 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 7/13 个有
- `1hew_TextToAny` —— 6/13 个有
- `Int` —— 6/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `MiniMaxH3PromptEnhancerT8` —— 6/13 个有
- `BasicScheduler` —— 5/13 个有
- `KSamplerSelect` —— 5/13 个有
- `MiniMaxH3ReferenceToVideo` —— 4/13 个有
- `VAEDecode` —— 4/13 个有
- `VAEDecodeAudio` —— 4/13 个有
- `忽略多组孤海` —— 4/13 个有
- `H3SigmaRefiner` —— 2/13 个有
- `LTXVConcatAVLatent` —— 2/13 个有
- `LTXVSeparateAVLatent` —— 2/13 个有
- `MiniMaxH3BlockCacheT8` —— 2/13 个有
- `MinimaxH3LatentUpscaler3D` —— 2/13 个有
- `PathchSageAttentionKJ` —— 2/13 个有
- `SplitSigmas` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `MiniMaxH3ImageToVideo` —— 1/13 个有
- `MiniMaxH3SigmaShift` —— 1/13 个有
- `PT_H3ConcatAVLatent` —— 1/13 个有
- `ResolutionSelector` —— 1/13 个有
- `VAEEncodeAudio` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有
- `easy imageSizeByLongerSide` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
