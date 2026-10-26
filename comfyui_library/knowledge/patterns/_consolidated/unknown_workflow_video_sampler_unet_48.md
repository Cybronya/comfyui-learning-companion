---
name: unknown_workflow_video_sampler_unet_48
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.580667
common_nodes: [BasicGuider, CLIPLoader, Fast Groups Bypasser (rgthree), GetNode, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/12号特工：minimaxH3四步加速双时钟+T8节点+图生视频+多参_2086057128527224833.json, 视频生成/图生视频/MiniMax H3全能参考（t8加速LORA）_2086006748221108225.json, 视频生成/图生视频/MiniMax H3文生视频+首尾帧生视频（t8加速LORA）_2086007059350380546.json, 视频生成/图生视频/MiniMax-H3 图生视频！ 加速版！_2085683743284621314.json, 视频生成/文生视频/MiniMax H3最新双涡轮增压4步Lora8步效果超极速工作流合集_2085545670534066177.json, 视频生成/文生视频/MiniMax-H3 文生视频！ 加速版！_2085652281692876802.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/12号特工：minimaxH3四步加速双时钟+T8节点+图生视频+多参_2086057128527224833.json、视频生成/图生视频/MiniMax H3全能参考（t8加速LORA）_2086006748221108225.json、视频生成/图生视频/MiniMax H3文生视频+首尾帧生视频（t8加速LORA）_2086007059350380546.json、视频生成/图生视频/MiniMax-H3 图生视频！ 加速版！_2085683743284621314.json、视频生成/文生视频/MiniMax H3最新双涡轮增压4步Lora8步效果超极速工作流合集_2085545670534066177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
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
- `ComfyMathExpression` —— 5/6 个有
- `LoraLoaderBypassModelOnly` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `Label (rgthree)` —— 3/6 个有
- `LoadVideo` —— 2/6 个有
- `Text` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `Float` —— 1/6 个有
- `Int` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `ttN int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
