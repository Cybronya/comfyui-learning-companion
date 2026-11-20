---
name: unknown_workflow_video_lora_sampler_96
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.613111
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json, 视频生成/图生视频/MiniMax H3数字人口播-图+音频生成口播视频工作流_2094979350235009025.json, 视频生成/图生视频/MiniMax+H3参考生视频-最强战斗效果-多图参考_2096436150956285954.json, 视频生成/图生视频/MiniMax+H3双采全能工作流V2-音频驱动数字人-参考生视频_2111113734084190209.json, 视频生成/图生视频/MiniMaxH3_双采参考生视频_2104941388239560705.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V2-音频驱动数字人-参考生视频_2100139084525166593.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V2-音频驱动数字人-参考生视频_2101871299831357442.json, 视频生成/图生视频/Minima-H3-武戏工作流_2108453082106515458.json, 视频生成/图生视频/Minimax H3文戏工作流_2114971114559598593.json, 视频生成/图生视频/MinimaxH3-场景图生视频丨短剧视频制作专用_2099413880610050049.json, 视频生成/图生视频/minimax H3 文戏工作流（急速版）_2106909033222459394.json, 视频生成/图生视频/minimaxH3 文武双修工作流_2114960907376873473.json, 视频生成/图生视频/minimaxh3高动文武双修工作流_2110566903226916866.json, 视频生成/图生视频/minimaxh3高动文武双修工作流_2111010562334355457.json, 视频生成/图生视频/【MINIMAX H3】武戏-高动态_极速高清_2107175289238409217.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏(修改版）_2103351056783728641.json, 视频生成/文生视频/minimax H3 文戏工作流（急速版）_2106909033222459394.json, 视频生成/文生视频/minimaxh3高动文武双修工作流_2106006102767915010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json、视频生成/图生视频/MiniMax H3数字人口播-图+音频生成口播视频工作流_2094979350235009025.json、视频生成/图生视频/MiniMax+H3参考生视频-最强战斗效果-多图参考_2096436150956285954.json、视频生成/图生视频/MiniMax+H3双采全能工作流V2-音频驱动数字人-参考生视频_2111113734084190209.json、视频生成/图生视频/MiniMaxH3_双采参考生视频_2104941388239560705.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 18 个 workflow 都包含：
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
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 17/18 个有
- `SolAttnMiniMax` —— 17/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 16/18 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 16/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 16/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 16/18 个有
- `GetNode` —— 14/18 个有
- `SetNode` —— 14/18 个有
- `Fast Groups Bypasser (rgthree)` —— 12/18 个有
- `Float` —— 12/18 个有
- `PreviewImage` —— 12/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/18 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 11/18 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 11/18 个有
- `ConcatTextOfUtils` —— 10/18 个有
- `VAEDecode` —— 8/18 个有
- `VAEDecodeAudio` —— 8/18 个有
- `easy cleanGpuUsed` —— 8/18 个有
- `LoadAudio` —— 7/18 个有
- `PreviewAny` —— 6/18 个有
- `RH_LLMAPI_Pro_Node` —— 6/18 个有
- `MiniMaxChunkFeedForward` —— 3/18 个有
- `MiniMaxLowVRAMAttention` —— 3/18 个有
- `忽略多组孤海` —— 2/18 个有
- `BasicScheduler` —— 1/18 个有
- `EmptyImage` —— 1/18 个有
- `ExtendIntermediateSigmas` —— 1/18 个有
- `H3SigmaRefiner` —— 1/18 个有
- `ImageResizeKJv2` —— 1/18 个有
- `KSamplerSelect` —— 1/18 个有
- `LTXVConcatAVLatent` —— 1/18 个有
- `VAEEncode` —— 1/18 个有
- `VAEEncodeAudio` —— 1/18 个有
- `easy anythingIndexSwitch` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
