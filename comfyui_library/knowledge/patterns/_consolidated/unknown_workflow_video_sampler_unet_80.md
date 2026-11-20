---
name: unknown_workflow_video_sampler_unet_80
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.76
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/minimax8步工作流_2101320025478098946.json, 视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json, 视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json, 视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/minimax8步工作流_2101320025478098946.json、视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json、视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json、视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/4 个有
- `MiniMaxH3PDD8StepSetupT8Advanced` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
