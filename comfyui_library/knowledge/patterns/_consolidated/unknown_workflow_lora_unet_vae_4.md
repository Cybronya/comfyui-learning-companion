---
name: unknown_workflow_lora_unet_vae_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.531667
common_nodes: [CLIPLoader, CM_BoolToInt, CR Prompt Text, ComfyMathExpression, CreateVideo, ExecutionBlocker, FloatToText, GetCurrentTimeNode, GetImageSize, GetNode, ImageScaleToTotalPixels, ImpactNeg, Int, IntConditions, JjkText, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3PromptEnhancerT8, PreviewAny, PrimitiveBoolean, PrimitiveFloat, RHLLMChatNode, RandomNoise, SaveAudioAdvanced, SaveLatent, SaveVideo, SetNode, StringReplace, UNETLoader, VAEEncode, VAELoader, easy anythingIndexSwitch, easy mathString, ttN concat, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+VDN+selflift 快速参考生视频_2097697625758846978.json, 视频生成/图生视频/MiniMax+VDN+selflift_快速参考生视频_2100927216665321474.json, 视频生成/图生视频/MiniMax-H3-VDN 快速参考生视频_2096530698105614337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax+VDN+selflift 快速参考生视频_2097697625758846978.json、视频生成/图生视频/MiniMax+VDN+selflift_快速参考生视频_2100927216665321474.json、视频生成/图生视频/MiniMax-H3-VDN 快速参考生视频_2096530698105614337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CM_BoolToInt`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `ExecutionBlocker`
- `FloatToText`
- `GetCurrentTimeNode`
- `GetImageSize`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImpactNeg`
- `Int`
- `IntConditions`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3PromptEnhancerT8`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `RandomNoise`
- `SaveAudioAdvanced`
- `SaveLatent`
- `SaveVideo`
- `SetNode`
- `StringReplace`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy mathString`
- `ttN concat`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `H3SigmaRefiner` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 2/3 个有
- `SelfLiftH3Sampler` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/3 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `SolAttnMiniMax` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
