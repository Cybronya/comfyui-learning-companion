---
name: unknown_workflow_video_sampler_unet_58
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6444
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json, 视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json, 视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json, 视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json, 视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json、视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json、视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json、视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json、视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoadAudio` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `GetNode` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `1hew_AnySwitchBool` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/5 个有
- `VRAMReserver` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
