---
name: unknown_workflow_video_upscale_latent_upscale_68
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.753667
common_nodes: [BasicGuider, CLIPLoader, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2103041925002653698.json, 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json, 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2092495104849309697.json, 视频生成/文生视频/xinlingjitang_2097652872459669506.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-高配版_2098584847945125889.json, 视频生成/文生视频/【二采-高配版】MinMaxh3日常短剧专用_2095187242611466242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_68

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2103041925002653698.json、视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json、视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2092495104849309697.json、视频生成/文生视频/xinlingjitang_2097652872459669506.json、视频生成/文生视频/【MINIMAX-H3】八月最强文戏-高配版_2098584847945125889.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
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
- `CR Prompt Text` —— 5/6 个有
- `ComfyMathExpression` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `GetNode` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `忽略多组孤海` —— 2/6 个有
- `1hew_AudioDuration` —— 1/6 个有
- `CR Load LoRA` —— 1/6 个有
- `FastGroupsBypassSwitch` —— 1/6 个有
- `Float` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
