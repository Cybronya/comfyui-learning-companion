---
name: unknown_workflow_video_lora_sampler_388
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.658833
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json, 视频生成/图生视频/多参考视频MINIMAX-H3工作流_2089733467306283009.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086780909889613825.json, 视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json, 视频生成/图生视频/自动化高质量多参视频流_2087788893096734722.json, 视频生成/文生视频/H3基础文生视频工作流_2101289589221715969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_388

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/基础 H3工作流-参考图逻辑判断版_2101186866648276994.json、视频生成/图生视频/多参考视频MINIMAX-H3工作流_2089733467306283009.json、视频生成/图生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086780909889613825.json、视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json、视频生成/图生视频/自动化高质量多参视频流_2087788893096734722.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `WujiCleaner` —— 1/6 个有
- `XB_ROCmMemCleaner` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
