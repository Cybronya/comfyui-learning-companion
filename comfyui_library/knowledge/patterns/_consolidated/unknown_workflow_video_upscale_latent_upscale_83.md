---
name: unknown_workflow_video_upscale_latent_upscale_83
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8488
common_nodes: [BasicGuider, CLIPLoader, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2103041925002653698.json, 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json, 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2092495104849309697.json, 视频生成/文生视频/动漫短剧文戏工作流（10eros+电影感lora）_2093873729087565825.json, 视频生成/文生视频/银河系小王minmaxh3-ForLoop多功能1至6段-视频续接V3V2_2094846710416756738.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_83

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2103041925002653698.json、视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json、视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2092495104849309697.json、视频生成/文生视频/动漫短剧文戏工作流（10eros+电影感lora）_2093873729087565825.json、视频生成/文生视频/银河系小王minmaxh3-ForLoop多功能1至6段-视频续接V3V2_2094846710416756738.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ComfyMathExpression` —— 4/5 个有
- `PrimitiveInt` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `CR Load LoRA` —— 1/5 个有
- `FastGroupsBypassSwitch` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `ImpactConditionalBranch` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `MiniMaxH3MotionContext` —— 1/5 个有
- `MiniMaxH3MotionContextTrim` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
