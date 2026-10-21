---
name: unknown_workflow_video_sampler_unet_60
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5048
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, GetNode, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/12号特工：minimaxH3四步加速双时钟+T8节点+图生视频+多参_2086057128527224833.json, 视频生成/图生视频/MiniMax H3全能参考（t8加速LORA）_2086006748221108225.json, 视频生成/图生视频/MiniMax H3文生视频+首尾帧生视频（t8加速LORA）_2086007059350380546.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/12号特工：minimaxH3四步加速双时钟+T8节点+图生视频+多参_2086057128527224833.json、视频生成/图生视频/MiniMax H3全能参考（t8加速LORA）_2086006748221108225.json、视频生成/图生视频/MiniMax H3文生视频+首尾帧生视频（t8加速LORA）_2086007059350380546.json、视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json、视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `GetNode`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoadAudio` —— 2/5 个有
- `Float` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxH3SigmaShift` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `ModelPreviewOverrideKJ` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `ttN int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
