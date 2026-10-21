---
name: unknown_workflow_video_lora_sampler_87
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.757188
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json, 视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-参考生视频_2093354886875406337.json, 视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json, 视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json, 视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json, 视频生成/图生视频/MiniMax H3 电商带货-双采全能工作流_2107862335695183874.json, 视频生成/图生视频/MiniMax H3-不油文剧工作流_2096934850723926018.json, 视频生成/图生视频/MiniMax H3-动态最强-参考生视频-V1_2094782408347447298.json, 视频生成/图生视频/MiniMax H3参考生视频-10Eros turbo动态叙事工作流_2095011453865652225.json, 视频生成/图生视频/MiniMax H3参考生视频-武戏战斗版_2098232096543297537.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-电商带货-参考生视频_2102717112467943425.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-参考生视频_2098795077903671298.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-电商带货-二采_2102718883990958081.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频_2105138065181339649.json, 视频生成/图生视频/MiniMax H3双采参考生视频支持参考音频和视频_2102401654355218433.json, 视频生成/图生视频/MiniMax H3双采参考生视频格莱美慢镜头_2103902789440196610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json、视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-参考生视频_2093354886875406337.json、视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json、视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json、视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：76%

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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/16 个有
- `ModelAttentionBackend` —— 15/16 个有
- `SolAttnMiniMax` —— 13/16 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 12/16 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 12/16 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 12/16 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 12/16 个有
- `LoraLoaderModelOnly` —— 11/16 个有
- `Float` —— 8/16 个有
- `孤海注释` —— 7/16 个有
- `GetNode` —— 6/16 个有
- `SetNode` —— 6/16 个有
- `ConcatTextOfUtils` —— 4/16 个有
- `Fast Groups Bypasser (rgthree)` —— 4/16 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/16 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/16 个有
- `LoadAudio` —— 3/16 个有
- `easy anythingIndexSwitch` —— 3/16 个有
- `VHS_LoadVideo` —— 2/16 个有
- `ExtendIntermediateSigmas` —— 1/16 个有
- `Fast Muter (rgthree)` —— 1/16 个有
- `H3SigmaRefiner` —— 1/16 个有
- `ImageCrop` —— 1/16 个有
- `ImageFromBatch` —— 1/16 个有
- `MiniMaxChunkFeedForward` —— 1/16 个有
- `MiniMaxLowVRAMAttention` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `TrimAudioDuration` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
