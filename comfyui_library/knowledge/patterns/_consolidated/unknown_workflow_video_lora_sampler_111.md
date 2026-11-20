---
name: unknown_workflow_video_lora_sampler_111
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.744188
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/(Dasiwa+V1+SLA加速)Minimax参考生视频V1_2092548650743455745.json, 图片生成/图生图/(双时钟-8步高质量极速)Minimax图生视频V1_2085659323732156418.json, 图片生成/图生图/(最佳动态)MiniMax H3Dasiwa HybirdV1+600EMA参考生视频V1_2093686271318253570.json, 图片生成/图生图/(长视频-文武双修均衡版-高清)MiniMax H3多参双采参考生视频_2103931824199266305.json, 图片生成/图生图/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2096774886025945089.json, 图片生成/图生图/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-文生视频_2104537651679420418.json, 平台全量/(长视频-文武双修均衡版-高清)MiniMax H3多参双采参考生视频_2105304143605878785.json, 平台全量/927(长视频-文武双修均衡版-高清)MiniMax H3多参双采参考生视频_2104185624218656770.json, 平台全量/H3 双采均衡与后置 VBVR_2119876675616989186.json, 平台全量/MiniMax H3双采全能工作流V4-VBVR逻辑强化-文戏不油，武戏动态强-参考生视频-长视频-高清直出_2118005769055596546.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频-长视频-视频复刻-高清直出_2109641176335863810.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-文生视频-长视频-高清有直出_2106198509325217793.json, 视频生成/图生视频/MiniMax H3双采全能工作流V4-VBVR逻辑强化-文戏不油，武戏动态强-参考生视频-长视频-高清直出_2113982579975221250.json, 视频生成/图生视频/MiniMax H3双采全能工作流V4-VBVR逻辑强化-文戏不油，武戏动态强-参考生视频-长视频-高清直出_2115451405820588034.json, 视频生成/文生视频/MiniMax H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频-长视频-高清有直出_2106353568906301442.json, 视频生成/文生视频/MiniMax H3双采全能工作流V4-VBVR逻辑强化-文戏不油，武戏动态强-文生视频-长视频-高清直出_2114001115871272961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/(Dasiwa+V1+SLA加速)Minimax参考生视频V1_2092548650743455745.json、图片生成/图生图/(双时钟-8步高质量极速)Minimax图生视频V1_2085659323732156418.json、图片生成/图生图/(最佳动态)MiniMax H3Dasiwa HybirdV1+600EMA参考生视频V1_2093686271318253570.json、图片生成/图生图/(长视频-文武双修均衡版-高清)MiniMax H3多参双采参考生视频_2103931824199266305.json、图片生成/图生图/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-参考生视频_2096774886025945089.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 15/16 个有
- `SolAttnMiniMax` —— 15/16 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 14/16 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 14/16 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 14/16 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 14/16 个有
- `Float` —— 13/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `Astra` —— 11/16 个有
- `CreateVideo` —— 11/16 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 11/16 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 11/16 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 11/16 个有
- `RunningHub Deepcleaner` —— 11/16 个有
- `SaveVideo` —— 11/16 个有
- `easy anythingIndexSwitch` —— 11/16 个有
- `easy cleanGpuUsed` —— 11/16 个有
- `GetNode` —— 9/16 个有
- `SetNode` —— 9/16 个有
- `孤海注释` —— 9/16 个有
- `Fast Groups Bypasser (rgthree)` —— 8/16 个有
- `ImpactFloat` —— 7/16 个有
- `Int` —— 7/16 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 7/16 个有
- `SimpleMath+` —— 7/16 个有
- `VAEDecode` —— 7/16 个有
- `BlockSparseAttention` —— 4/16 个有
- `AnyBooleanSwitch` —— 2/16 个有
- `CR Font File List` —— 2/16 个有
- `CompressImages` —— 2/16 个有
- `ImpactConditionalBranch` —— 2/16 个有
- `LoadFolderFromDir` —— 2/16 个有
- `MiniMaxH3ActivationChunkT8Advanced` —— 2/16 个有
- `VHS_SelectFilename` —— 2/16 个有
- `LoadAudio` —— 1/16 个有
- `LoadVideo` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `Vignette` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
