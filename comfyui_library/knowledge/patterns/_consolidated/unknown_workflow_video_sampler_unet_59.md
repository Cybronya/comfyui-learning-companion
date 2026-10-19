---
name: unknown_workflow_video_sampler_unet_59
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4514
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, GetNode, LoadImage, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【官模】H3风格测试 _ 案例2：各国早餐（风格）_2093549585775026177.json, 视频生成/图生视频/【官模】首尾帧 _ H3案例：科普小视频（一颗土豆的故事🥔）_2091398589313544193.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人_2100778688936759297.json, 视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json, 视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【官模】H3风格测试 _ 案例2：各国早餐（风格）_2093549585775026177.json、视频生成/图生视频/【官模】首尾帧 _ H3案例：科普小视频（一颗土豆的故事🥔）_2091398589313544193.json、视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人_2100778688936759297.json、视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json、视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `GetNode`
- `LoadImage`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `KSamplerSelect` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `LoadAudio` —— 3/5 个有
- `LoraLoaderBypassModelOnly` —— 3/5 个有
- `MiniMaxH3AudioConditioningT8` —— 3/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `SolAttnMiniMax` —— 3/5 个有
- `ComfySwitchNodeV2` —— 2/5 个有
- `Int` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `MiniMaxChunkFeedForward` —— 2/5 个有
- `MiniMaxH3ReferenceToVideo` —— 2/5 个有
- `MiniMaxLowVRAMAttention` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `MiniMaxH3AVDecodeT8` —— 1/5 个有
- `MiniMaxH3AddGuide` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
