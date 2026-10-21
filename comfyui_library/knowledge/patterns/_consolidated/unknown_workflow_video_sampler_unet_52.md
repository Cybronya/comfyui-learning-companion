---
name: unknown_workflow_video_sampler_unet_52
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.683714
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json, 视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json, 视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json, 视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json, 视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json, 视频生成/文生视频/MINIMAX-H3 全能参考生成视频｜文生｜图生｜首尾帧｜尾帧｜首帧_2085961446109831169.json, 视频生成/文生视频/MiniMax+H3！加速版！提速480%！全能参考！_2085641752681213953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json、视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json、视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json、视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json、视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `LoraLoaderBypassModelOnly` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ModelPreviewOverrideKJ` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `1hew_AnySwitchBool` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/7 个有
- `VRAMReserver` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
