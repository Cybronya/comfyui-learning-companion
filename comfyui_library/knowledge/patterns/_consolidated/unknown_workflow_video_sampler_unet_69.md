---
name: unknown_workflow_video_sampler_unet_69
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.473667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【官模】H3风格测试 _ 案例2：各国早餐（风格）_2093549585775026177.json, 视频生成/图生视频/【官模】首尾帧 _ H3案例：科普小视频（一颗土豆的故事🥔）_2091398589313544193.json, 视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【官模】H3风格测试 _ 案例2：各国早餐（风格）_2093549585775026177.json、视频生成/图生视频/【官模】首尾帧 _ H3案例：科普小视频（一颗土豆的故事🥔）_2091398589313544193.json、视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNodeV2` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `MiniMaxH3AudioConditioningT8` —— 2/3 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/3 个有
- `SolAttnMiniMax` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `ModelPreviewOverrideKJ` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
