---
name: unknown_workflow_video_lora_sampler_169
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.721077
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/8步高质量极速Minimax_H3开源版_2114989406414266369.json, 图片生成/图生图/Minimax_H3_4图参考生视频-双时钟采样-8步极速版_2087145478369660929.json, 图片生成/图生图/Minimax图生视频V2(双时钟-8步高质量极速）_2087465694903492610.json, 图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2098949863919673345.json, 图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2099061501553373185.json, 图片生成/图生图/武侠打斗丨MiniMax H3丨多图参考·有声视频_2112107703127601154.json, 平台全量/武侠打斗丨MiniMax_H3丨多图参考·有声视频_2118960161040723969.json, 数字人/数字人/（28秒）MiniMax H3双采参考生视频V1_2104395488899461122.json, 视频生成/图生视频/(语义桥-枪战-文武双修均衡版V3)MiniMax H3双采参考生视频_2100787934323625986.json, 视频生成/图生视频/MINIMAX H3 -高动态武戏-全自动-极速高清输出_2104934302449491970.json, 视频生成/图生视频/MINIMAXH3-武戏高动态二采工作流_Aiforly_2110713376044314626.json, 视频生成/图生视频/MINIMAXH3武戏高动态二采工作流_Aiforly｜高动态武戏专用_2114686173607190530.json, 视频生成/文生视频/9月30日目前最强武戏-高动态_极速高清_ 自动提示词+手动提示词2选1_2104942695335682050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/8步高质量极速Minimax_H3开源版_2114989406414266369.json、图片生成/图生图/Minimax_H3_4图参考生视频-双时钟采样-8步极速版_2087145478369660929.json、图片生成/图生图/Minimax图生视频V2(双时钟-8步高质量极速）_2087465694903492610.json、图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2098949863919673345.json、图片生成/图生图/【MINIMAX-H3】八月最强文戏-高配版_2099061501553373185.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 12/13 个有
- `ModelAttentionBackend` —— 12/13 个有
- `ResolutionSelector` —— 12/13 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 10/13 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 10/13 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 10/13 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 10/13 个有
- `SolAttnMiniMax` —— 10/13 个有
- `PreviewImage` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 8/13 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 8/13 个有
- `ConcatTextOfUtils` —— 6/13 个有
- `Float` —— 6/13 个有
- `GetNode` —— 6/13 个有
- `SetNode` —— 6/13 个有
- `LoadAudio` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `PreviewAny` —— 4/13 个有
- `RH_LLMAPI_Pro_Node` —— 4/13 个有
- `PrimitiveStringMultiline` —— 3/13 个有
- `ComfySwitchNode` —— 2/13 个有
- `EmptyImage` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxLowVRAMAttention` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `easy anythingIndexSwitch` —— 2/13 个有
- `忽略多组孤海` —— 2/13 个有
- `ImpactSwitch` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `Text Multiline` —— 1/13 个有
- `easy int` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
